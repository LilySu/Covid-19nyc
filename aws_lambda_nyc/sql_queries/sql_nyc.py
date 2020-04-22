from sqlalchemy import create_engine
import mysql.connector
import pandas as pd
import psycopg2
#Local Imports
from extract_data.get_new_nyc_borough_confirmed import get_borough_confirmed
from combine.combine_nyc import combine_scraped_and_historical
# from wrangle.wrangle_nyc_from_counties import wrangle_nyc_percentage_daily_change
# from wrangle.wrangle_counties import wrangle_counties_new_daily_cases #,wrangle_counties_for_timeslider


engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres2.chtkfsooypac.us-east-1.rds.amazonaws.com:5432/postgres', echo=False)

def store_historical_nyc():
    df = get_borough_confirmed()
    df.to_sql(name='historical_nyc_table', con=engine, index=False, if_exists="replace")
#if_exists options: {‘fail’, ‘replace’, ‘append’}, default ‘fail’

def execute_combine_nyc_scraped_and_historical():
    df = combine_scraped_and_historical()
    df.to_sql(name='combined_nyc_table', con=engine, index=False, if_exists="append")

# def execute_wrangle_nyc_percentage_daily_change():
#     df_nyc_percentage_daily_change = wrangle_nyc_percentage_daily_change()
#     df_nyc_percentage_daily_change.to_sql(name='nyc_percentage_daily_change_table', con=engine, index=False, if_exists="replace")
#     df_nyc_percentage_daily_change.to_sql(name='test_nyc_percentage_daily_change_table', con=engine, index=False, if_exists="append")

# def execute_wrangle_counties_new_daily_cases():
#     df_counties_new_daily_cases = wrangle_counties_new_daily_cases()
#     df_counties_new_daily_cases.to_sql(name='counties_new_daily_cases_table', con=engine, index=False, if_exists="replace")
#     df_counties_new_daily_cases.to_sql(name='test_counties_new_daily_cases_table', con=engine, index=False, if_exists="append")

# def execute_wrangle_counties_for_timeslider():
#     df_counties_for_timeslider = wrangle_counties_for_timeslider()
#     df_counties_for_timeslider.to_sql(name='counties_for_timeslider_table', con=engine, index=False, if_exists="replace")