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
    execute_scrape_counties_wikipedia()
    # execute_combine_counties_scraped_and_historical()
    # execute_wrangle_nyc_percentage_daily_change()
    # execute_wrangle_counties_new_daily_cases()
    return 'Hello execute_scrape_counties_wikipedia() has been executed'
    


































