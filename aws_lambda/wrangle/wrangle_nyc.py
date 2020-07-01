from datetime import datetime, date, time, timedelta
import pytz
from pytz import timezone
import pandas as pd
import numpy as np 

from sql_queries.sql_get_nyc_nys_socrata import get_nys_data


def get_nyc_latest():
    """
    -county header has 1 value only which is New York City
    -Returns dataframe dfcity_only that is only 1 row with headers:
    
    test_date | county | new_positives | cumulative_number_of_positives | total_number_of_tests | lastupdate

    """
    df = get_nys_data()
    dfc = df[(df['county']=='New York')|(df['county']=='Bronx')|(df['county']=='Queens')|(df['county']=='Kings')|(df['county']=='Richmond')]
    dfc['new_positives'] = pd.to_numeric(dfc['new_positives'], errors='coerce')
    dfc['cumulative_number_of_positives'] = pd.to_numeric(dfc['cumulative_number_of_positives'], errors='coerce')
    dfc['total_number_of_tests'] = pd.to_numeric(dfc['total_number_of_tests'], errors='coerce')
    dfc['cumulative_number_of_tests'] = pd.to_numeric(dfc['cumulative_number_of_tests'], errors='coerce')
    dfc = dfc.append(dfc.sum(numeric_only=True), ignore_index=True)
    dfc.at[5,'test_date'] = df['test_date'][0]
    dfc.at[5,'county'] = 'New York City'
    dfcity_only = dfc.iloc[5:6]
    dfcity_only['lastupdate'] = datetime.now(tz=pytz.timezone('US/Eastern'))
    dfcity_only['lastupdate'] = dfcity_only['lastupdate'].apply(lambda x: x.strftime('%B %d %I:%M %p'))
    return dfcity_only