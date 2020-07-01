from sqlalchemy import create_engine
import mysql.connector
import pandas as pd
import psycopg2
#Local Imports
from extract_data.get_new_nyc_borough_confirmed import get_borough_confirmed
from combine.combine_nyc import combine_scraped_and_historical

engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres2.chtkfsooypac.us-east-1.rds.amazonaws.com:5432/postgres', echo=False)

def store_historical_nyc():
    df = get_borough_confirmed()
    df.to_sql(name='historical_nyc_table', con=engine, index=False, if_exists="replace")
#if_exists options: {‘fail’, ‘replace’, ‘append’}, default ‘fail’

def execute_combine_nyc_scraped_and_historical():
    dn, df = combine_scraped_and_historical()
    if dn is not None:
        dn.to_sql(name='combined_nyc_table', con=engine, index=False, if_exists="replace")
        df.to_sql(name='historical_nyc_table', con=engine, index=False, if_exists="replace")