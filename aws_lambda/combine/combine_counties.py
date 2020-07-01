import time
from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np 
#Local Imports
#from static.historical_counties_df import wrangle_historical_county_df # just in case there needs to be manual tweaks
from sql_queries.sql_get_counties import get_scraped_counties, get_historic_counties_records, get_combined_counties # gets df, df_confirmed_historical_T
import pytz


def combine_counties_scraped_and_historical():
    """ 
    1. Updates combined_county_table by concatenating scraped with combined table.
    2. Returns a df with confirmed cases by county, date in the format of Month-day like 
    April 08, and a total
    3. Has commented out options to pull from historic table from database or 
    wrangle from scratch from static > historical_counties_df.py up to April 08th.
    4. Log datetime in another table
    """
  
    # df_confirmed_historical_T = get_historic_counties_records()# get historical data from database so toggle between this line and the next 
      
      
    data = get_combined_counties()
    df_confirmed_historical_T = pd.DataFrame(data, columns=['Albany', 'Allegany', 'Bronx', 'Broome', 'Cattaraugus', 'Cayuga',
        'Chautauqua', 'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland',
        'Delaware', 'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton',
        'Genesee', 'Greene', 'Hamilton', 'Herkimer', 'Jefferson', 'Kings',
        'Lewis', 'Livingston', 'Madison', 'Monroe', 'Montgomery', 'Nassau',
        'New York', 'Niagara', 'Oneida', 'Onondaga', 'Ontario', 'Orange',
        'Orleans', 'Oswego', 'Otsego', 'Putnam', 'Queens', 'Rensselaer',
        'Richmond', 'Rockland', 'Saratoga', 'Schenectady', 'Schoharie',
        'Schuyler', 'Seneca', 'St. Lawrence', 'Steuben', 'Suffolk', 'Sullivan',
        'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington', 'Wayne',
        'Westchester', 'Wyoming', 'Yates','date','total'])
    df_confirmed_historical_T.reset_index(drop=True, inplace=True) # reset index for later retrieval of the latest numbers to compare if there was an update
    
    
    data = get_scraped_counties()
    #Todo retrieve column headers from database
    df = pd.DataFrame(data, columns=['County', 'Confirmed', 'Deaths', 'Recoveries', 'Population','lastupdate'])
    df = df.T
    df = df.reset_index()
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df = df.rename(columns={'County': 'Status'})
    df.loc[:,'date'] = datetime.now(tz=pytz.timezone('EST'))# - timedelta(days=1) # for yesterday
    df.loc[:,'date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')
    df.loc[:,'date'] = df['date'].apply(lambda x: x.strftime('%B %d'))
    df.loc[:,'Status'] = df['Status'].str.replace(' ', '')
    df_confirmed = df[df['Status']=='Confirmed'] # filters in df_confirmed only Confirmed cases
    del df
    cols = df_confirmed.columns.drop(['Status','date'])
    # df_confirmed.loc[:,cols] = df_confirmed[cols].apply(pd.to_numeric, errors='coerce', downcast='signed')# convert to int
    df_confirmed.loc[:,cols] = df_confirmed[cols].astype('int')
    df_for_total = df_confirmed.drop(columns = ['date','Status'])
      
    df_confirmed['total'] = df_for_total.sum(axis=1)
    del df_for_total
    
    last_historical_nyc_num = df_confirmed_historical_T['New York'][0]
    [scraped_nyc_num] = df_confirmed['New York City'].values.T.tolist()
    
    if last_historical_nyc_num < scraped_nyc_num: # if this update showed a different nyc number from before
        df_confirmed = df_confirmed.loc[:,~df_confirmed.columns.duplicated()]
        # match wikipedia scrape
        df_confirmed.loc[:,'New York'] = df_confirmed['New York City'] 
        df_confirmed.loc[:,'Queens'] = df_confirmed['New York']
        df_confirmed.loc[:,'Kings'] = df_confirmed['New York']
        df_confirmed.loc[:,'Richmond'] = df_confirmed['New York']
        df_confirmed.loc[:,'Bronx'] = df_confirmed['New York']
        df_confirmed.drop(columns=['Status','New York City'], inplace=True)
        df_confirmed = pd.concat([df_confirmed,df_confirmed_historical_T],axis=0, ignore_index=True, sort=True) #combine tables
        del df_confirmed_historical_T
        current_time = datetime.now(tz=pytz.timezone('EST'))
        current_time = current_time.strftime('%B %d, %Y %H:%M')
        df_confirmed.at[0,'Albany'] = 619 ###################################### bandaid solution
        return df_confirmed, current_time; # return a tuple of the newly combined dataframe and current update time as a string
    
    else:
        print(f'The last confirmed number for nyc is: {last_historical_nyc_num}, and the just scraped confirmed number for nyc is: {scraped_nyc_num}')
        return None, None;
