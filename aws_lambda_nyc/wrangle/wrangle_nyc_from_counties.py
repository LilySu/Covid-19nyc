import pandas as pd
import numpy as np 
#Local Imports
from sql_queries.sql_get import get_combined_counties # gets df_confirmed


def wrangle_nyc_percentage_daily_change():
    df_confirmed = get_combined_counties()
    df_confirmed = pd.DataFrame(df_confirmed, columns=['Albany', 'Allegany', 'Broome', 'Cattaraugus', 'Cayuga', 'Chautauqua',
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

    df_confirmed_r = df_confirmed.iloc[::-1]

    df_confirmed_r = df_confirmed_r[['Albany', 'Allegany', 'Broome', 'Cattaraugus', 'Cayuga', 'Chautauqua',
        'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland', 'Delaware',
        'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton', 'Genesee', 'Greene',
        'Hamilton', 'Herkimer', 'Jefferson', 'Lewis', 'Livingston', 'Madison',
        'Monroe', 'Montgomery', 'Nassau', 'Niagara', 'Oneida', 'Onondaga',
        'Ontario', 'Orange', 'Orleans', 'Oswego', 'Otsego', 'Putnam',
        'Rensselaer', 'Rockland', 'Saratoga', 'Schenectady', 'Schoharie',
        'Schuyler', 'Seneca', 'St Lawrence', 'Steuben', 'Suffolk', 'Sullivan',
        'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington', 'Wayne',
        'Westchester', 'Wyoming', 'Yates', 'New York', 'Queens',
        'Kings', 'Richmond', 'Bronx']]
    df_confirmed_r = df_confirmed_r.astype('float64')
    ddiff = df_confirmed_r.diff()
    df_confirmed_r = ddiff/df_confirmed_r
    df_confirmed_r = df_confirmed_r.fillna(0)
    df_confirmed_r = df_confirmed_r.replace(np.inf, 0)
    df_confirmed_r = df_confirmed_r.replace(-np.inf, 0)

    dc = df_confirmed.iloc[::-1]
    del df_confirmed
    dates = list(dc['date'])
    del dc
    df_confirmed_r['date'] = dates

    df_nyc_percentage_changes = df_confirmed_r[['New York','date']]
    del df_confirmed_r
    df_nyc_percentage_changes['New York'] = pd.Series([round(val, 2) for val in df_nyc_percentage_changes['New York']], index = df_nyc_percentage_changes.index)
    df_nyc_percentage_changes['New York'] = pd.Series(["{0:.0f}%".format(val * 100) for val in df_nyc_percentage_changes['New York']], index = df_nyc_percentage_changes.index)
    return df_nyc_percentage_changes