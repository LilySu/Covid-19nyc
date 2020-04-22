import time
from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np 
#Local Imports
#from static.historical_counties_df import wrangle_historical_county_df # just in case there needs to be manual tweaks
from sql_queries.sql_get import get_historical_nyc_data
import pytz


def combine_scraped_and_historical():
    lastupdate = datetime.now(tz=pytz.timezone('EST')) - timedelta(days=1) 
    lastupdate = lastupdate.strftime('%B %d' )

    today = datetime.now(tz=pytz.timezone('EST'))
    today = today.strftime('%B %d' )

    df_new = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/boro.csv')
    df_new = df_new[['BOROUGH_GROUP', 'COVID_CASE_COUNT']]
    df_new.rename(columns={'COVID_CASE_COUNT':today}, inplace=True)

    data = get_historical_nyc_data()
    headers = ['BOROUGH_GROUP', 'March 22', 'March 23', 'March 24', 'March 25',
       'March 26', 'March 27', 'March 28', 'March 29', 'March 30', 'March 31',
       'April 01', 'April 02', 'April 03', 'April 04', 'April 05', 'April 06',
       'April 07', 'April 08', 'April 09', 'April 10', 'April 11', 'April 12',
       'April 13', 'April 14', 'April 15', 'April 16', 'April 17', 'April 18',
       'April 19']
    df = pd.DataFrame(data, columns=headers)

    if df[lastupdate][2] < df_new[today][2]:
        df = df.merge(df_new, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
        return df
