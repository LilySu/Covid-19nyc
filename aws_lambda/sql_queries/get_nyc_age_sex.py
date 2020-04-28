from datetime import datetime, date, time, timedelta
from sqlalchemy import create_engine
from pytz import timezone
import mysql.connector
import pandas as pd
import psycopg2
import pytz

engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres2.chtkfsooypac.us-east-1.rds.amazonaws.com:5432/postgres', echo=False)

def get_age_nyc_data():
  sql = f'''
  SELECT * 
  FROM age_nyc_table;
  '''
  with engine.connect() as conn:
    return [record for record in conn.execute(sql)]
    
def get_sex_nyc_data():
  sql = f'''
  SELECT * 
  FROM sex_nyc_table;
  '''
  with engine.connect() as conn:
    return [record for record in conn.execute(sql)]