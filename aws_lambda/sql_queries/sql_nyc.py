from datetime import datetime, date, time, timedelta
from sqlalchemy import create_engine
from pytz import timezone
import mysql.connector
import pandas as pd
import psycopg2
import pytz

#Local Imports
from extract_data.get_new_nyc_borough_confirmed import get_borough_confirmed
from combine.combine_nyc import combine_scraped_and_historical
from sql_queries.get_nyc_age_sex import get_age_nyc_data
from sql_queries.get_nyc_age_sex import get_sex_nyc_data


engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres2.chtkfsooypac.us-east-1.rds.amazonaws.com:5432/postgres', echo=False)
current_time = datetime.now(tz=pytz.timezone('EST'))
current_time = current_time.strftime('%B %d, %Y %H:%M')
        
def store_historical_nyc():
    df = get_borough_confirmed()
    df.to_sql(name='historical_nyc_table', con=engine, index=False, if_exists="replace")
#if_exists options: {‘fail’, ‘replace’, ‘append’}, default ‘fail’

def execute_combine_nyc_scraped_and_historical():
    dn, df = combine_scraped_and_historical()
    if dn is not None:
        dn.to_sql(name='combined_nyc_table', con=engine, index=False, if_exists="replace")
        df.to_sql(name='historical_nyc_table', con=engine, index=False, if_exists="replace")
        logdict = {'combine_nyc_table_changed_on':[current_time]}
        df_update_log = pd.DataFrame(data = logdict)
        df_update_log.to_sql(name='log_nyc_table', con=engine, index=False, if_exists="append")
        
def execute_update_age_nyc():
    data = get_age_nyc_data()
    headers = ['AGE_GROUP', 'COVID_CASE_RATE', 'HOSPITALIZED_CASE_RATE', 'DEATH_RATE']
    age = pd.DataFrame(data, columns=headers)
    age.to_sql(name='age_nyc_table', con=engine, index=False, if_exists="replace")
    
def execute_update_sex_nyc():
    data = get_sex_nyc_data()
    headers = ['AGE_GROUP', 'COVID_CASE_RATE', 'HOSPITALIZED_CASE_RATE', 'DEATH_RATE']
    sex = pd.DataFrame(data, columns=headers)
    sex.to_sql(name='sex_nyc_table', con=engine, index=False, if_exists="replace")