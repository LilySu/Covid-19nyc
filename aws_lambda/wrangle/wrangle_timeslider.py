import pandas as pd
import numpy as np 
#Local Imports
from sql_queries.sql_get_counties import get_combined_counties # gets df_confirmed
from sql_queries.sql_get_counties import get_historical_county_data


def wrangle_counties_for_timeslider():
    """ 
    -Dataframe is formatted for Plotly timeslider
    -Each county has its own row for each day since March 1
    -Each date has its own column
    -Boroughs of nyc are all totals for all 5 boroughts
    -county | March 1 | date | March 2 | March 3 | ... | June 26 | June 27 | total | total_normalized | county_full
    """
    df_confirmed_historical_T = get_historical_county_data()
    a = df_confirmed_historical_T.T
    a = a.reset_index()
    a.columns = a.iloc[-2]
    a = a.drop(a.index[-2])
    a.rename(columns={'date':'county'}, inplace=True)
    collist = a.columns.drop(['county'])
    c = a[['county','April 18']]
    c['date'] = 'April 18'
    for i in collist:
      b = a[['county',i]]
      b['date'] = i
      c = pd.concat([b,c], axis=0, sort=False)
    c.fillna(0, inplace=True)
    c = c.drop_duplicates()
    df = c
    collist = c.columns.drop(['county','date'])
    for i in collist:
        df[i] = df[i].fillna(0)
        df[i] = df[i].astype('float64')
    df['total'] = df[collist].sum(axis=1)
    df['total_normalized'] = np.log10(df["total"])
    df['county_full'] = df['county'] + ' County'
    return df