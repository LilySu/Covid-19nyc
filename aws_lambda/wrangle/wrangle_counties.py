from datetime import datetime, date, time, timedelta
import pytz
from pytz import timezone
import pandas as pd
import numpy as np 
#Local Imports
from sql_queries.sql_get_counties import get_combined_counties # gets df_confirmed
from sql_queries.sql_get_counties import get_historical_county_data
from sql_queries.sql_get_nyc_nys_socrata import get_nys_data 
from wrangle.wrangle_nyc import get_nyc_latest

def wrangle_sodapy_one_row_new_counties_data():
    df_latest = get_nys_data()
    dft = df_latest.T
    dft = dft.reset_index()
    dft.columns = dft.iloc[1]
    dft = dft.drop(dft.index[1])
    dft = dft.rename(columns={'county': 'Status'})
    dft.loc[:,'date'] = datetime.now(tz=pytz.timezone('US/Eastern'))# - timedelta(days=1) # for yesterday
    dft.loc[:,'date'] = dft['date'].apply(lambda x: x.strftime('%B %d'))
    dft = dft[2:3]
    dfcity_only = get_nyc_latest()
    nyc_cumulative_positive = dfcity_only['cumulative_number_of_positives'][5]
    dft['New York City'] = nyc_cumulative_positive
    return dft

def wrangle_combine_counties_with_new_socrata_update():

    """ 
    -Concatenates the 1 row of latest county numbers with historical county numbers
    -Counties are in alphabetical order
    -Boroughs of nyc are all totals for all 5 boroughts
    -Albany | Allegany | Bronx | ... | Yates | date | total
    """
    df_confirmed_historical_T = get_historical_county_data()
    df_confirmed = wrangle_sodapy_one_row_new_counties_data()
    cols = df_confirmed.columns.drop(['Status','date'])
    df_confirmed.loc[:,cols] = df_confirmed[cols].astype('int')
    df_for_total = df_confirmed.drop(columns = ['date','Status'])    
    df_confirmed['total'] = df_for_total.sum(axis=1)
    del df_for_total
    df_confirmed=df_confirmed.loc[:,~df_confirmed.columns.duplicated()]
    # unifies each instance of boroughs into New York City
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
    return df_confirmed


def wrangle_counties_new_daily_cases():
    """ 
    -Number of new cases from previous day
    -Absolute values are taken if there are discrepancies especially days surrounding May 4
    -Counties are in alphabetical order
    -Boroughs of nyc are all totals for all 5 boroughts
    -Albany | Allegany | Bronx | ... | Yates | date | total
    """
    df_confirmed = get_historical_county_data()
    df_confirmed_r = df_confirmed.iloc[::-1]
    df_confirmed_r = df_confirmed_r[['Albany', 'Allegany', 'Broome', 'Cattaraugus', 'Cayuga', 'Chautauqua',
        'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland', 'Delaware',
        'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton', 'Genesee', 'Greene',
        'Hamilton', 'Herkimer', 'Jefferson', 'Lewis', 'Livingston', 'Madison',
        'Monroe', 'Montgomery', 'Nassau', 'Niagara', 'Oneida', 'Onondaga',
        'Ontario', 'Orange', 'Orleans', 'Oswego', 'Otsego', 'Putnam',
        'Rensselaer', 'Rockland', 'Saratoga', 'Schenectady', 'Schoharie',
        'Schuyler', 'Seneca', 'St. Lawrence', 'Steuben', 'Suffolk', 'Sullivan',
        'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington', 'Wayne',
        'Westchester', 'Wyoming', 'Yates', 'New York', 'Queens',
        'Kings', 'Richmond', 'Bronx']]
    df_confirmed_r = df_confirmed_r.astype('float64')
    ddiff = df_confirmed_r.diff()
    del df_confirmed_r
    dc = df_confirmed.iloc[::-1]
    dates = list(dc['date'])
    del df_confirmed
    ddiff['date'] = dates
    ddiff['total'] = ddiff[['Albany', 'Allegany', 'Broome', 'Cattaraugus', 'Cayuga', 'Chautauqua',
        'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland', 'Delaware',
        'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton', 'Genesee', 'Greene',
        'Hamilton', 'Herkimer', 'Jefferson', 'Lewis', 'Livingston', 'Madison',
        'Monroe', 'Montgomery', 'Nassau', 'Niagara', 'Oneida', 'Onondaga',
        'Ontario', 'Orange', 'Orleans', 'Oswego', 'Otsego', 'Putnam',
        'Rensselaer', 'Rockland', 'Saratoga', 'Schenectady', 'Schoharie',
        'Schuyler', 'Seneca', 'St. Lawrence', 'Steuben', 'Suffolk', 'Sullivan',
        'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington', 'Wayne',
        'Westchester', 'Wyoming', 'Yates', 'New York']].sum(axis=1)
    ddiff['average'] = ddiff[['Albany', 'Allegany', 'Broome', 'Cattaraugus', 'Cayuga', 'Chautauqua',
        'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland', 'Delaware',
        'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton', 'Genesee', 'Greene',
        'Hamilton', 'Herkimer', 'Jefferson', 'Lewis', 'Livingston', 'Madison',
        'Monroe', 'Montgomery', 'Nassau', 'Niagara', 'Oneida', 'Onondaga',
        'Ontario', 'Orange', 'Orleans', 'Oswego', 'Otsego', 'Putnam',
        'Rensselaer', 'Rockland', 'Saratoga', 'Schenectady', 'Schoharie',
        'Schuyler', 'Seneca', 'St. Lawrence', 'Steuben', 'Suffolk', 'Sullivan',
        'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington', 'Wayne',
        'Westchester', 'Wyoming', 'Yates', 'New York']].mean(axis=1)
    ddiff.fillna(0, inplace=True)
    ddiff['average'] = ddiff['average'].round(0)
    return ddiff
