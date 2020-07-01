import pandas as pd
import numpy as np



def update_nyc_zipcode_data():
    df = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/tests-by-zcta.csv',dtype={'MODZCTA': 'str'})
    df = df.fillna(0)
    llzip = pd.read_csv('https://gist.githubusercontent.com/erichurst/7882666/raw/5bdc46db47d9515269ab12ed6fb2850377fd869e/US%2520Zip%2520Codes%2520from%25202013%2520Government%2520Data',dtype={'ZIP': 'str'})
    zipnames = pd.read_csv('https://covidnyc.s3.us-east-1.amazonaws.com/df_nyc/uszips.csv',dtype={'zip': 'str'})
    df = df.merge(llzip, left_on='MODZCTA', right_on='ZIP',how='inner')
    df = df.merge(zipnames, left_on='MODZCTA',right_on='zip')
    df['Positive_Percentage_of_Population'] = (df['Positive']/df['population'])*100
    return df