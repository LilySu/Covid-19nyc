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
    1. Replaces combined_county_table with updated version of scraped plus historical data.
    2. Returns a df with confirmed cases by county, date in the format of Month-day like 
    April 08, and a total"""

    df = get_scraped_counties()# get info from database
    df = pd.DataFrame(df, columns=['County', 'Confirmed', 'Deaths', 'Recoveries', 'Population','Deaths2Confirmed', 'Confirmed2Population','lastupdate'])
    df = df.drop(columns=['lastupdate'])
    # df_confirmed_historical_T = get_historic_counties_records()# get from database
    # df_confirmed_historical_T = pd.DataFrame(df_confirmed_historical_T, columns=['date', 'Albany', 'Allegany', 'Bronx', 'Broome', 'Cattaraugus',
    #   'Cayuga', 'Chautauqua', 'Chemung', 'Chenango', 'Clinton', 'Columbia',
    #   'Cortland', 'Delaware', 'Dutchess', 'Erie', 'Essex', 'Franklin',
    #   'Fulton', 'Genesee', 'Greene', 'Hamilton', 'Herkimer', 'Jefferson',
    #   'Kings', 'Lewis', 'Livingston', 'Madison', 'Monroe', 'Montgomery',
    #   'Nassau', 'New York', 'Niagara', 'Oneida', 'Onondaga', 'Ontario',
    #   'Orange', 'Orleans', 'Oswego', 'Otsego', 'Putnam', 'Queens',
    #   'Rensselaer', 'Richmond', 'Rockland', 'Saratoga', 'Schenectady',
    #   'Schoharie', 'Schuyler', 'Seneca', 'St Lawrence', 'Steuben', 'Suffolk',
    #   'Sullivan', 'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington',
    #   'Wayne', 'Westchester', 'Wyoming', 'Yates'])
    df_confirmed_historical_T = get_combined_counties()# get from database
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
       
    # df_confirmed_historical_T = wrangle_historical_county_df()# for custom changes
    
    df = df.T
    df = df.reset_index()
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df = df.rename(columns={'County': 'Status'})
    
    df['lastupdated'] = datetime.now(tz=pytz.timezone('EST'))
    # import datetime
    # df['lastupdated'] = df['lastupdated'] - datetime.timedelta(days=1)
    df['date'] = pd.to_datetime(df['lastupdated'], format = '%Y-%m-%d')
    df['date'] = df['date'].apply(lambda x: x.strftime('%B %d'))
    df['Status'] = df['Status'].str.replace(' ', '')
    collist = ['Albany', 'Allegany', 'Broome', 'Cattaraugus', 'Cayuga',
               'Chautauqua', 'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland',
               'Delaware', 'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton',
               'Genesee', 'Greene', 'Hamilton', 'Herkimer', 'Jefferson', 'Lewis',
               'Livingston', 'Madison', 'Monroe', 'Montgomery', 'Nassau', 'Niagara',
               'Oneida', 'Onondaga', 'Ontario', 'Orange', 'Orleans', 'Oswego',
               'Otsego', 'Putnam', 'Rensselaer', 'Rockland', 'Saratoga', 'Schenectady',
               'Schoharie', 'Schuyler', 'Seneca', 'St Lawrence', 'Steuben', 'Suffolk',
               'Sullivan', 'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington',
               'Wayne', 'Westchester', 'Wyoming', 'Yates', 'New York City a']
    try:
        for i in collist:
          df[i] = df[i].str.replace(' ', '')
          df[i] = df[i].str.replace(',', '')
          df[i] = df[i].fillna(0)
          df[i] = df[i].astype('float64')
    except AttributeError as e:
        pass
    df_confirmed = df[df['Status']=='Confirmed']
    del df
    df_confirmed['New York'] = df_confirmed['New York City a']
    df_confirmed['Queens'] = df_confirmed['New York']
    df_confirmed['Kings'] = df_confirmed['New York']
    df_confirmed['Richmond'] = df_confirmed['New York']
    df_confirmed['Bronx'] = df_confirmed['New York']
    # df_confirmed = pd.concat([df_confirmed,df_confirmed_historical_T], sort=False, keys=['date','New York'])
    df_confirmed = pd.concat([df_confirmed, df_confirmed_historical_T], axis=0)
    df_confirmed['New York City a'] = df_confirmed['New York']
    # del df_confirmed_historical_T
    df_confirmed = df_confirmed.drop(['lastupdated'], axis=1)
    df_confirmed = df_confirmed.drop(['New York City a'], axis=1)
    df_confirmed = df_confirmed.drop(['Status'], axis=1)
    df_confirmed['total'] = df_confirmed[['Albany', 'Allegany', 'Broome', 'Cattaraugus', 'Cayuga', 'Chautauqua',
        'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland', 'Delaware',
        'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton', 'Genesee', 'Greene',
        'Hamilton', 'Herkimer', 'Jefferson', 'Lewis', 'Livingston', 'Madison',
        'Monroe', 'Montgomery', 'Nassau', 'Niagara', 'Oneida', 'Onondaga',
        'Ontario', 'Orange', 'Orleans', 'Oswego', 'Otsego', 'Putnam',
        'Rensselaer', 'Rockland', 'Saratoga', 'Schenectady', 'Schoharie',
        'Schuyler', 'Seneca', 'St Lawrence', 'Steuben', 'Suffolk', 'Sullivan',
        'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington', 'Wayne',
        'Westchester', 'Wyoming', 'Yates', 'New York']].sum(axis=1)
    return df_confirmed
