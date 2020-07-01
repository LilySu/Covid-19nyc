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
    
    today = datetime.now(tz=pytz.timezone('EST')) # - timedelta(days=1)
    today = today.strftime('%B %d' )

    df_new = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/by-boro.csv')
    df_new = df_new[['BOROUGH_GROUP', 'CASE_COUNT']]
    df_new.rename(columns={'CASE_COUNT':today,'BOROUGH_GROUP':'boro_name'}, inplace=True)
    df_new['boro_name'][0] = 'Bronx'
    df_new['boro_name'][4] = 'Staten Island'
    df_new['boro_name'][5] = 'total'
    df_new = df_new.T
    df_new = df_new.reset_index()
    df_new.columns = df_new.iloc[0]
    df_new = df_new.drop(df_new.index[0])
    df_new.rename(columns={'boro_name':'date'}, inplace=True)
    # df_new = df_new.head()
    # May 20 update
    # df_new = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/boro/boroughs-by-age.csv')
    # df_new = pd.DataFrame({'date':[today], 'Bronx': [df_new['BX_CASE_COUNT'][5]],'Brooklyn':[df_new['BK_CASE_COUNT'][5]], 'Manhattan':[df_new['MN_CASE_COUNT'][5]], 'Queens':[df_new['QN_CASE_COUNT'][5]], 'Staten Island':[df_new['SI_CASE_COUNT'][5]]})
    # df_new['total'] = df_new[['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']].sum(axis=1)


    data = get_historical_nyc_data()
    # # IF I WANT TO MANUALLY ADD I HAVE TO UPDATE THIS TO REFLECT THE ACTUAL HEADER
    # headers = ['BOROUGH_GROUP', 'March 22', 'March 23', 'March 24', 'March 25',
    #   'March 26', 'March 27', 'March 28', 'March 29', 'March 30', 'March 31',
    #   'April 01', 'April 02', 'April 03', 'April 04', 'April 05', 'April 06',
    #   'April 07', 'April 08', 'April 09', 'April 10', 'April 11', 'April 12',
    #   'April 13', 'April 14', 'April 15', 'April 16', 'April 17', 'April 18',
    #   'April 19', 'April 20', 'April 21', 'April 22', 'April 23', 'April 24'] 
    # headers = date_list
    try: 
        # df = pd.DataFrame(data, columns=['BOROUGH_GROUP']+headers)
        df = pd.DataFrame(data, columns = ['date', 'Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island','total'])
    except ValueError:
        print('historical table might already have updated information from today')

    # lastupdate = headers[-1]

    if df['total'].iloc[-1] < df_new['total'][0]:
        # df = df.merge(df_new, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
        # del df
        # return df
        # dn = df.T
        # dn = dn.reset_index()
        # dn.columns = dn.iloc[0]
        # dn = dn.drop(dn.index[0])
        # dn = dn.rename(columns={'BOROUGH_GROUP': 'date', 'The Bronx':'Bronx'})
        # collist = ['Bronx','Brooklyn','Manhattan','Queens','Staten Island']
        
        
        # dn['total'] = dn[collist].astype(int).sum(axis=1)
        df = pd.concat([df, df_new], axis=0)
        return df
    # return df_new
