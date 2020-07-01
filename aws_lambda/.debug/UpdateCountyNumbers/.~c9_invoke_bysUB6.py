from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask import Flask
from os import environ
#Local Imports
from sql_queries.sql_counties import execute_scrape_counties_wikipedia
from sql_queries.sql_counties import execute_combine_counties_scraped_and_historical
from sql_queries.sql_counties import execute_wrangle_nyc_percentage_daily_change
from sql_queries.sql_counties import execute_wrangle_counties_new_daily_cases


def lambda_handler(event, context):
    execute_scrape_counties_wikipedia() # scraped_county_table
    # execute_combine_counties_scraped_and_historical() # combined_county_table
    # execute_wrangle_nyc_percentage_daily_change() # nyc_percentage_daily_change_table
    # execute_wrangle_counties_new_daily_cases() # counties_new_daily_cases_table
    return 'Lambda function has been executed'
    
