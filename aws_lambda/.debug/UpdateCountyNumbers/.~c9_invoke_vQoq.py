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


def lambda_handler(event, context):
    stop_event = Event()
 
    def delay_actions():
        """
        Function that implements timeout
        """
        while True:
            
            # execute_scrape_counties_wikipedia() # scraped_county_table
            
            # time.sleep(7)
            
            execute_combine_counties_scraped_and_historical() # combined_county_table
            
            # time.sleep(7)
            
            # execute_wrangle_nyc_percentage_daily_change() # nyc_percentage_daily_change_table
            
            # time.sleep(2)
            
            # execute_wrangle_counties_new_daily_cases() # counties_new_daily_cases_table
    
            if stop_event.is_set():
                break
    action_thread = Thread(target=delay_actions)
    action_thread.start()
    action_thread.join(timeout=5)
    stop_event.set()
    
    return 'Lambda function has been executed'
    
