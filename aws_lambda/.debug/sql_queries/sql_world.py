from datetime import datetime, date, time, timedelta
from sqlalchemy import create_engine
from pytz import timezone
import mysql.connector
import pandas as pd
import psycopg2
import pytz

#Local Imports
from extract_data.get_world import get_updated_world_data


engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres2.chtkfsooypac.us-east-1.rds.amazonaws.com:5432/postgres', echo=False)
current_time = datetime.now(tz=pytz.timezone('EST'))
current_time = current_time.strftime('%B %d, %Y %H:%M')


def execute_update_world():
    world_dict = get_updated_world_data()
    df_italy = world_dict['italy']
    df_china = world_dict['china']
    df_usa = world_dict['usa']
    df_italy.to_sql(name='world_italy_table', con=engine, index=False, if_exists="replace")
    df_china.to_sql(name='world_china_table', con=engine, index=False, if_exists="replace")
    df_usa.to_sql(name='world_usa_table', con=engine, index=False, if_exists="replace")
    logdict = {'world_tables_updated_on':[current_time]}
    df_update_log = pd.DataFrame(data = logdict)
    df_update_log.to_sql(name='log_world_tables', con=engine, index=False, if_exists="append")