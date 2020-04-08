from sqlalchemy import create_engine
import mysql.connector
import pandas as pd
import psycopg2
#Local Imports
from scrape.scrape_counties import scrape_counties_wikipedia
<<<<<<< HEAD
from combine.combine_counties import combine_counties_scraped_and_historical
from wrangle.wrangle_nyc_from_counties import wrangle_nyc_percentage_daily_change
from wrangle.wrangle_counties import wrangle_counties_new_daily_cases,wrangle_counties_for_timeslider
=======
<<<<<<< HEAD
from combine.combine_counties import combine_counties_scraped_and_historical
from wrangle.wrangle_nyc_from_counties import wrangle_nyc_percentage_daily_change
from wrangle.wrangle_counties import wrangle_counties_new_daily_cases,wrangle_counties_for_timeslider
=======
>>>>>>> c81f5b724ad603ab6a4211138c394a31d3772a1a
>>>>>>> c0f2f0148f3e325198cff97d8b51209bf3e82636


engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres2.chtkfsooypac.us-east-1.rds.amazonaws.com:5432/postgres', echo=False)

def execute_scrape_counties_wikipedia():
    df = scrape_counties_wikipedia()
<<<<<<< HEAD
    df.to_sql(name='county_table', con=engine, index=False, if_exists="append")
#if_exists options: {‘fail’, ‘replace’, ‘append’}, default ‘fail’

def get_scraped_counties():
  sql = f'''
  SELECT * 
  FROM county_table;
  '''
  with engine.connect() as conn:
    return [record for record in conn.execute(sql)]

def get_combined_counties():
  sql = f'''
  SELECT * 
  FROM combined_county_table;
  '''
  with engine.connect() as conn:
    return [record for record in conn.execute(sql)]

def execute_combine_counties_scraped_and_historical():
    df_counties_scraped_and_historical = combine_counties_scraped_and_historical()
    df_counties_scraped_and_historical.to_sql(name='combined_county_table', con=engine, index=False, if_exists="replace")

def execute_wrangle_nyc_percentage_daily_change():
    df_nyc_percentage_daily_change = wrangle_nyc_percentage_daily_change()
    df_nyc_percentage_daily_change.to_sql(name='nyc_percentage_daily_change_table', con=engine, index=False, if_exists="replace")

def execute_wrangle_counties_new_daily_cases():
    df_counties_new_daily_cases = wrangle_counties_new_daily_cases()
    df_counties_new_daily_cases.to_sql(name='counties_new_daily_cases_county_table', con=engine, index=False, if_exists="replace")

def execute_wrangle_counties_for_timeslider():
    df_counties_for_timeslider = wrangle_counties_for_timeslider()
    df_counties_for_timeslider.to_sql(name='counties_for_timeslider_table', con=engine, index=False, if_exists="replace")
=======
<<<<<<< HEAD
    df.to_sql(name='county_table', con=engine, index=False, if_exists="append")
#if_exists options: {‘fail’, ‘replace’, ‘append’}, default ‘fail’

def get_scraped_counties():
  sql = f'''
  SELECT * 
  FROM county_table;
  '''
  with engine.connect() as conn:
    return [record for record in conn.execute(sql)]

def get_combined_counties():
  sql = f'''
  SELECT * 
  FROM combined_county_table;
  '''
  with engine.connect() as conn:
    return [record for record in conn.execute(sql)]

def execute_combine_counties_scraped_and_historical():
    df_counties_scraped_and_historical = combine_counties_scraped_and_historical()
    df_counties_scraped_and_historical.to_sql(name='combined_county_table', con=engine, index=False, if_exists="replace")

def execute_wrangle_nyc_percentage_daily_change():
    df_nyc_percentage_daily_change = wrangle_nyc_percentage_daily_change()
    df_nyc_percentage_daily_change.to_sql(name='nyc_percentage_daily_change_table', con=engine, index=False, if_exists="replace")

def execute_wrangle_counties_new_daily_cases():
    df_counties_new_daily_cases = wrangle_counties_new_daily_cases()
    df_counties_new_daily_cases.to_sql(name='counties_new_daily_cases_county_table', con=engine, index=False, if_exists="replace")

def execute_wrangle_counties_for_timeslider():
    df_counties_for_timeslider = wrangle_counties_for_timeslider()
    df_counties_for_timeslider.to_sql(name='counties_for_timeslider_table', con=engine, index=False, if_exists="replace")
=======
    df.to_sql(name='county_table', con=engine, index=False, if_exists="replace")
#if_exists options: {‘fail’, ‘replace’, ‘append’}, default ‘fail’
>>>>>>> c81f5b724ad603ab6a4211138c394a31d3772a1a
>>>>>>> c0f2f0148f3e325198cff97d8b51209bf3e82636
