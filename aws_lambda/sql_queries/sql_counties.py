from datetime import datetime, date, time, timedelta
from sqlalchemy import create_engine
import pytz
from pytz import timezone
import mysql.connector
import pandas as pd
import psycopg2
#Local Imports
from wrangle.wrangle_nyc_from_counties import wrangle_nyc_percentage_daily_change
from wrangle.wrangle_counties import wrangle_counties_new_daily_cases, wrangle_combine_counties_with_new_socrata_update
from wrangle.wrangle_timeslider import wrangle_counties_for_timeslider
from wrangle.wrangle_nyc import get_nyc_latest

engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres2.chtkfsooypac.us-east-1.rds.amazonaws.com:5432/postgres', echo=False)
current_time = datetime.now(tz=pytz.timezone('EST'))
current_time = current_time.strftime('%B %d, %Y %H:%M')

def execute_get_nyc_update():
    df = get_nyc_latest()
    df.to_sql(name='nyc_latest', con=engine, index=False, if_exists="replace")

def execute_get_all_counties_latest():
    df = get_nys_data()
    df.to_sql(name='all_counties_latest', con=engine, index=False, if_exists="replace")

def execute_combine_counties():
    df_combined = wrangle_combine_counties_with_new_socrata_update()
    df_combined.to_sql(name='combined_county_table', con=engine, index=False, if_exists="replace")
    logdict = {'combine_county_table_changed_on':[current_time]}
    df_update_log = pd.DataFrame(data = logdict)
    df_update_log.to_sql(name='log_combined_county_table', con=engine, index=False, if_exists="append")

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

execute_wrangle_counties_timeslider()