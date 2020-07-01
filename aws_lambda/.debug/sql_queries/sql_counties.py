from sqlalchemy import create_engine
import mysql.connector
import pandas as pd
import psycopg2
#Local Imports
from scrape.scrape_counties import scrape_counties_wikipedia
from combine.combine_counties import combine_counties_scraped_and_historical
from wrangle.wrangle_nyc_from_counties import wrangle_nyc_percentage_daily_change
from wrangle.wrangle_counties import wrangle_counties_new_daily_cases
from wrangle.wrangle_timeslider import wrangle_counties_for_timeslider


engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres2.chtkfsooypac.us-east-1.rds.amazonaws.com:5432/postgres', echo=False)

def execute_scrape_counties_wikipedia():
    df = scrape_counties_wikipedia()
    df.to_sql(name='scraped_county_table', con=engine, index=False, if_exists="replace")
    # df.to_sql(name='test_scraped_county_table', con=engine, index=False, if_exists="append")
#if_exists options: {‘fail’, ‘replace’, ‘append’}, default ‘fail’

def execute_combine_counties_scraped_and_historical():
    df_counties_scraped_and_historical, current_time = combine_counties_scraped_and_historical()
    if df_counties_scraped_and_historical is not None: #if data is updated, is not None
        df_counties_scraped_and_historical.to_sql(name='combined_county_table', con=engine, index=False, if_exists="replace")
        logdict = {'combine_county_table_changed_on':[current_time]}
        df_update_log = pd.DataFrame(data = logdict)
        df_update_log.to_sql(name='log_combined_county_table', con=engine, index=False, if_exists="append")
        # df_counties_scraped_and_historical.to_sql(name='test_combined_county_table', con=engine, index=False, if_exists="append")

def execute_wrangle_nyc_percentage_daily_change():
    df_nyc_percentage_daily_change = wrangle_nyc_percentage_daily_change()
    df_nyc_percentage_daily_change.to_sql(name='nyc_percentage_daily_change_table', con=engine, index=False, if_exists="replace")
    # df_nyc_percentage_daily_change.to_sql(name='nyc_percentage_daily_change_table', con=engine, index=False, if_exists="append")

def execute_wrangle_counties_new_daily_cases():
    df_counties_new_daily_cases = wrangle_counties_new_daily_cases()
    df_counties_new_daily_cases.to_sql(name='counties_new_daily_cases_table', con=engine, index=False, if_exists="replace")
    # df_counties_new_daily_cases.to_sql(name='test_counties_new_daily_cases_table', con=engine, index=False, if_exists="append")

def execute_wrangle_counties_timeslider():
    df_counties_for_timeslider = wrangle_counties_for_timeslider()
    df_counties_for_timeslider.to_sql(name='counties_timeslider_table', con=engine, index=False, if_exists="replace")