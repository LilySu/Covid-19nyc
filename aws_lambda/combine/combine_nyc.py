import time
from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np 
#Local Imports
#from static.historical_nyc_df import wrangle_historical_nyc_df # just in case there needs to be manual tweaks
from sql_queries.sql_get_counties import get_historical_nyc_data
import pytz
from pytz import timezone


def combine_scraped_and_historical():
    lastupdate = datetime.now(tz=pytz.timezone('EST')) - timedelta(days=1) 
    lastupdate = lastupdate.strftime('%B %d' )
    
    first_date_recorded = 'March 23 2020'
    first_date_recorded = datetime.strptime(first_date_recorded,'%B %d %Y')
    first_date_recorded = first_date_recorded.astimezone(timezone('UTC'))
    
    today_for_range = datetime.now(timezone('UTC')) - timedelta(days=1)# assumes latest date is yesterday
    date_list = pd.date_range(first_date_recorded, today_for_range).tolist()
    date_list = [i.astimezone(timezone('EST')) for i in date_list]
    date_list = [i.strftime('%B %d') for i in date_list]
    
    today = datetime.now(tz=pytz.timezone('EST'))
    today = today.strftime('%B %d' )

    df_new = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/boro.csv')
    df_new = df_new[['BOROUGH_GROUP', 'COVID_CASE_COUNT']]
    df_new.rename(columns={'COVID_CASE_COUNT':today}, inplace=True)
    df_new = df_new.head()

    data = get_historical_nyc_data()
    # # IF I WANT TO MANUALLY ADD I HAVE TO UPDATE THIS TO REFLECT THE ACTUAL HEADER
    # headers = ['BOROUGH_GROUP', 'March 22', 'March 23', 'March 24', 'March 25',
    #   'March 26', 'March 27', 'March 28', 'March 29', 'March 30', 'March 31',
    #   'April 01', 'April 02', 'April 03', 'April 04', 'April 05', 'April 06',
    #   'April 07', 'April 08', 'April 09', 'April 10', 'April 11', 'April 12',
    #   'April 13', 'April 14', 'April 15', 'April 16', 'April 17', 'April 18',
    #   'April 19', 'April 20', 'April 21', 'April 22', 'April 23', 'April 24'] 
    headers = date_list
    try: 
        df = pd.DataFrame(data, columns=['BOROUGH_GROUP']+headers)
    except ValueError:
        print('historical table might already have updated information from today')

    # lastupdate = headers[-1]

    if df[lastupdate][2] < df_new[today][2]:
        df = df.merge(df_new, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
        # del df
        # return df
        dn = df.T
        dn = dn.reset_index()
        dn.columns = dn.iloc[0]
        dn = dn.drop(dn.index[0])
        dn = dn.rename(columns={'BOROUGH_GROUP': 'date', 'The Bronx':'Bronx'})
        collist = ['Bronx','Brooklyn','Manhattan','Queens','Staten Island']
        dn['total'] = dn[collist].astype(int).sum(axis=1)
        return dn, df
    # return df_new
