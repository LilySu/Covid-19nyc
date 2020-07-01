from flask_sqlalchemy import SQLAlchemy
from threading import Thread, Event
from sqlalchemy.sql import func
from flask import Flask
from os import environ
import time
#Local Imports
from sql_queries.sql_counties import execute_scrape_counties_wikipedia
from sql_queries.sql_counties import execute_combine_counties_scraped_and_historical
from sql_queries.sql_counties import execute_wrangle_nyc_percentage_daily_change
from sql_queries.sql_counties import execute_wrangle_counties_new_daily_cases
from sql_queries.sql_counties import execute_wrangle_counties_timeslider
from sql_queries.sql_nyc import store_historical_nyc
from sql_queries.sql_nyc import execute_combine_nyc_scraped_and_historical
from sql_queries.sql_nyc import execute_update_age_nyc
from sql_queries.sql_nyc import execute_update_sex_nyc
from sql_queries.sql_nyc import execute_update_zipcode_nyc
from sql_queries.sql_world import execute_update_world

def lambda_handler(event, context):
    stop_event = Event()
 
    def delay_actions():
        """
        Function that implements timeout
        """
        while True:
            
            ##### New York State ######
            
            # execute_scrape_counties_wikipedia() # scraped_county_table # Scraiping blocked from wikipedia
            
            # time.sleep(10)
            #################################################
            
            execute_combine_counties_scraped_and_historical() # combined_county_table
            
            time.sleep(5)
            
            execute_wrangle_nyc_percentage_daily_change() # nyc_percentage_daily_change_table
            
            time.sleep(1)
            
            execute_wrangle_counties_new_daily_cases() # counties_new_daily_cases_table
            
            time.sleep(1)
            
            execute_wrangle_counties_timeslider() # counties_timeslider_table
            
            
            ##### NYC ###### CONFIRMED
    
            # store_historical_nyc() #ONLY FOR RESET and pulling from historical
            
            # time.sleep(5)
            
            execute_combine_nyc_scraped_and_historical()
            time.sleep(3)
            
            ##### NYC ###### FOR PIE CHARTS
            
            execute_update_age_nyc()
            
            execute_update_sex_nyc()
            time.sleep(2)
            
            ##### NYC ###### ZIPCODES
            
            execute_update_zipcode_nyc()
            time.sleep(2)
            
            ##### WORLD #####
            execute_update_world() #works when everything commented out
            
            if stop_event.is_set():
                break
    action_thread = Thread(target=delay_actions)
    action_thread.start()
    action_thread.join(timeout=5)
    stop_event.set()
    
    return 'Lambda function has been executed'
    
