from flask_sqlalchemy import SQLAlchemy
from threading import Thread, Event
from sqlalchemy.sql import func
from flask import Flask
from os import environ
import time
#Local Imports
from sql_queries.sql_counties import execute_get_nyc_update
from sql_queries.sql_counties import execute_combine_counties
from sql_queries.sql_counties import execute_wrangle_nyc_percentage_daily_change
from sql_queries.sql_counties import execute_wrangle_counties_new_daily_cases
from sql_queries.sql_counties import execute_wrangle_counties_timeslider
from sql_queries.sql_counties import execute_get_all_counties_latest
from sql_queries.sql_nyc import execute_update_age_nyc
from sql_queries.sql_nyc import execute_update_sex_nyc
from sql_queries.sql_nyc import execute_update_zipcode_nyc
from sql_queries.sql_world import execute_update_world
from wrange.wrangle_check_needs_update import wrangle_check_update



def lambda_handler(event, context):
    stop_event = Event()
 
    def delay_actions():
        """
        Function that implements timeout
        """
        while True:
            
           # #### NYC ###### FOR PIE CHARTS            
            execute_update_age_nyc()           
            execute_update_sex_nyc()
            time.sleep(1)
            
            # ##### NYC ###### ZIPCODES            
            execute_update_zipcode_nyc()
            time.sleep(5)
            
            # # ##### WORLD #####
            execute_update_world() #works when everything commented out
            time.sleep(15)

            # ##### NYC and New York State Based on State Dept of Health ######
            new_york_state_status = wrangle_check_update():
            if new_york_state_status == 'Needs Update':

                execute_get_nyc_update()           
                time.sleep(2)
                execute_get_all_counties_latest()
                time.sleep(2)
                execute_combine_counties()
                time.sleep(5)
                execute_wrangle_nyc_percentage_daily_change() # nyc_percentage_daily_change_table                
                time.sleep(1)                
                execute_wrangle_counties_new_daily_cases() # counties_new_daily_cases_table               
                time.sleep(1)               
                execute_wrangle_counties_timeslider() # counties_timeslider_table
            
            if stop_event.is_set():
                break
    action_thread = Thread(target=delay_actions)
    action_thread.start()
    action_thread.join(timeout=5)
    stop_event.set()
    
    return 'Lambda function has been executed'
    
