import time
from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np 
#Local Imports
#from static.historical_counties_df import wrangle_historical_county_df # just in case there needs to be manual tweaks
from sql_queries.sql_get import get_scraped_counties, get_historic_counties_records, get_combined_counties # gets df, df_confirmed_historical_T
import pytz


def combine_counties_scraped_and_historical():
    """ 
    1. Updates combined_county_table by concatenating scraped with combined table.
    2. Returns a df with confirmed cases by county, date in the format of Month-day like 
    April 08, and a total
    3. Has commented out options to pull from historic table from database or 
    wrangle from scratch from static > historical_counties_df.py up to April 08th.
    """

    df = get_scraped_counties()# get scraped info from database
    df = pd.DataFrame(df, columns=['County', 'Confirmed', 'Deaths', 'Recoveries', 'Population','Deaths2Confirmed', 'Confirmed2Population','lastupdate'])
    df = df.drop(columns=['lastupdate'])
    # df_confirmed_historical_T = get_historic_counties_records()# get historical data from database
    df_confirmed_historical_T = get_combined_counties()# get combined table from from database
    df_confirmed_historical_T = pd.DataFrame(df_confirmed_historical_T, columns=['Albany', 'Allegany', 'Broome', 'Cattaraugus', 'Cayuga', 'Chautauqua',
       'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland', 'Delaware',
       'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton', 'Genesee', 'Greene',
       'Hamilton', 'Herkimer', 'Jefferson', 'Lewis', 'Livingston', 'Madison',
       'Monroe', 'Montgomery', 'Nassau', 'Niagara', 'Oneida', 'Onondaga',
       'Ontario', 'Orange', 'Orleans', 'Oswego', 'Otsego', 'Putnam',
       'Rensselaer', 'Rockland', 'Saratoga', 'Schenectady', 'Schoharie',
       'Schuyler', 'Seneca', 'St Lawrence', 'Steuben', 'Suffolk', 'Sullivan',
       'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington', 'Wayne',
       'Westchester', 'Wyoming', 'Yates', 'date', 'New York', 'Queens',
       'Kings', 'Richmond', 'Bronx', 'total'])
    # df_confirmed_historical_T = wrangle_historical_county_df()# for custom changes - option to wrangle from scratch
    
    df = df.T
    df = df.reset_index()
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df = df.rename(columns={'County': 'Status'})
    df.loc[:,'lastupdated'] = datetime.now(tz=pytz.timezone('EST'))
    df.loc[:,'date'] = pd.to_datetime(df['lastupdated'], format = '%Y-%m-%d') # this is not needed 
    df.loc[:,'date'] = df['date'].apply(lambda x: x.strftime('%B %d'))
    df.loc[:,'Status'] = df['Status'].str.replace(' ', '')
    # df.loc[:,'total'] = df[['Albany', 'Allegany', 'Broome', 'Cattaraugus', 'Cayuga', 'Chautauqua',
    #   'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland', 'Delaware',
    #   'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton', 'Genesee', 'Greene',
    #   'Hamilton', 'Herkimer', 'Jefferson', 'Lewis', 'Livingston', 'Madison',
    #   'Monroe', 'Montgomery', 'Nassau', 'Niagara', 'Oneida', 'Onondaga',
    #   'Ontario', 'Orange', 'Orleans', 'Oswego', 'Otsego', 'Putnam',
    #   'Rensselaer', 'Rockland', 'Saratoga', 'Schenectady', 'Schoharie',
    #   'Schuyler', 'Seneca', 'St Lawrence', 'Steuben', 'Suffolk', 'Sullivan',
    #   'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington', 'Wayne',
    #   'Westchester', 'Wyoming', 'Yates', 'New York City a']].sum()
    df_confirmed = df[df['Status']=='Confirmed'] # filters in df_confirmed only Confirmed cases
    del df
    df_confirmed=df_confirmed.loc[:,~df_confirmed.columns.duplicated()]
    df_confirmed.loc[:,'New York'] = df_confirmed['New York City a'] # matches wikipedia scrape, may need to be changed later
    df_confirmed.loc[:,'Queens'] = df_confirmed['New York']
    df_confirmed.loc[:,'Kings'] = df_confirmed['New York']
    df_confirmed.loc[:,'Richmond'] = df_confirmed['New York']
    df_confirmed.loc[:,'Bronx'] = df_confirmed['New York']
    df_confirmed = pd.concat([df_confirmed_historical_T,df_confirmed])
    df_confirmed.drop(columns=['Status','New York City a', 'lastupdated'], inplace=True)
    return df_confirmed
