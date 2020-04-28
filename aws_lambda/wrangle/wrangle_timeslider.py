import pandas as pd
import numpy as np 
#Local Imports
from sql_queries.sql_get import get_combined_counties # gets df_confirmed


def wrangle_counties_for_timeslider():
    df_confirmed = get_combined_counties()
    df_confirmed = pd.DataFrame(df_confirmed, columns=['Albany', 'Allegany', 'Bronx', 'Broome', 'Cattaraugus', 'Cayuga',
       'Chautauqua', 'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland',
       'Delaware', 'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton',
       'Genesee', 'Greene', 'Hamilton', 'Herkimer', 'Jefferson', 'Kings',
       'Lewis', 'Livingston', 'Madison', 'Monroe', 'Montgomery', 'Nassau',
       'New York', 'Niagara', 'Oneida', 'Onondaga', 'Ontario', 'Orange',
       'Orleans', 'Oswego', 'Otsego', 'Putnam', 'Queens', 'Rensselaer',
       'Richmond', 'Rockland', 'Saratoga', 'Schenectady', 'Schoharie',
       'Schuyler', 'Seneca', 'St Lawrence', 'Steuben', 'Suffolk', 'Sullivan',
       'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington', 'Wayne',
       'Westchester', 'Wyoming', 'Yates','date','total'])
    df_combined_t = df_confirmed.T
    df_combined_t = df_combined_t.reset_index()
    df_combined_t.columns = df_combined_t.iloc[-2]
    df_combined_t = df_combined_t.drop(df_combined_t.index[-2])
    df_combined_t.rename(columns={'date':'county'}, inplace=True)
    collist = df_combined_t.columns.drop(['county'])
    
    df = df_combined_t[['county','March 22']]
    df['date'] = 'March 22'
    for i in collist:
      df_for_appending = df_combined_t[['county',i]]
      df_for_appending['date'] = i
      df = pd.concat([df_for_appending,df], axis=0, sort=False)
    df.fillna(0, inplace=True)
    collist = df.columns.drop(['county','date'])
    
    
    
    collist = df.columns.drop(['county','date'])
    for i in collist:
        df[i] = df[i].fillna(0)
        df[i] = df[i].astype('float64')
    df['total'] = df[collist].sum(axis=1)
    df['total_normalized'] = np.log10(df["total"])
    df['county'] = df['county'].str.replace('St Lawrence', 'St. Lawrence')
    df['county_full'] = df['county'] + ' County'
    return df