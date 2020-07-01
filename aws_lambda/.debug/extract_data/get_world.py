from datetime import datetime, date, time, timedelta
import pandas as pd
import numpy as np
import requests
import pytz
from pytz import timezone


def get_updated_world_data():
    first_date_recorded = 'January 22 2020'
    first_date_recorded = datetime.strptime(first_date_recorded,'%B %d %Y')
    first_date_recorded = first_date_recorded.astimezone(timezone('UTC')) + timedelta(days=1)
    
    today_for_range = datetime.now(timezone('UTC')) - timedelta(days=1)
    date_list_dt = pd.date_range(first_date_recorded, today_for_range).tolist()
    date_list_dt = [i.astimezone(timezone('EST')) for i in date_list_dt]
    date_list = [i.strftime('%m-%d-%Y') for i in date_list_dt]
    
    df_names_list = ["df-"+i.strftime('%m-%d-%Y') for i in date_list_dt]
    
    world_df_list = []
    for date_string, dataframe_name in zip(date_list, df_names_list):
         dataframe_name = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"+ date_string +".csv")
         dataframe_name['date'] = date_string
         world_df_list.append(dataframe_name)
    df = pd.concat(world_df_list, sort=False)
    
    df['Country_Region'].fillna(df['Country/Region'], inplace=True)
    df['Province/State'].fillna(df['Province_State'], inplace=True)
    df['Combined_Key'] = df['Province_State'] + ' ' + df['Country_Region']
    df['Lat'].fillna(df['Latitude'], inplace=True)
    df['Long_'].fillna(df['Longitude'], inplace=True)
    df.drop(columns=['Province/State','Country/Region','Latitude','Longitude','Last_Update','Active','Admin2','Last Update','Incidence_Rate','Case-Fatality_Ratio'], inplace=True)
    
    df.fillna(0, inplace=True)
    df['FIPS'] = df['FIPS'].astype(int)
    
    df = df.reset_index()
    
    df['log_conf'] = np.log10(df['Confirmed'])**2
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)
    def remove_zeros(column):
      column = str(column)
      if column == '0':
        column = ''
      return column
    
    df_italy = df[df['Country_Region']=='Italy']
    df_italy = df_italy.groupby('date').sum()
    df_italy = df_italy.reset_index()
    df_italy.at[41, 'Confirmed']= 12463.0	
    df_italy['new_Confirmed'] = df_italy['Confirmed'].diff().fillna(0)
    df_italy['new_Recovered'] = df_italy['Recovered'].diff().fillna(0)
    df_italy['new_Deaths'] = df_italy['Deaths'].diff().fillna(0)
    df_italy['p_new_Confirmed'] = df_italy['new_Confirmed']/df_italy['Confirmed']
    df_italy['p_new_Recovered'] = df_italy['new_Recovered']/df_italy['Recovered']
    df_italy['p_new_Deaths'] = df_italy['new_Deaths']/df_italy['Deaths']
    
    df_usa = df[df['Country_Region']=='US']
    df_usa = df_usa.groupby('date').sum()
    df_usa = df_usa.reset_index()
    df_usa['new_Confirmed'] = df_usa['Confirmed'].diff().fillna(0)
    df_usa['new_Recovered'] = df_usa['Recovered'].diff().fillna(0)
    df_usa['new_Deaths'] = df_usa['Deaths'].diff().fillna(0)
    df_usa['p_new_Confirmed'] = df_usa['new_Confirmed']/df_usa['Confirmed']
    df_usa['p_new_Recovered'] = df_usa['new_Recovered']/df_usa['Recovered']
    df_usa['p_new_Deaths'] = df_usa['new_Deaths']/df_usa['Deaths']
    
    df_china = df[(df['Country_Region']=='Mainland China') | (df['Country_Region']=='China')]
    df_china = df_china.groupby('date').sum()
    df_china = df_china.reset_index()
    df_china['new_Confirmed'] = df_china['Confirmed'].diff().fillna(0)
    df_china['new_Recovered'] = df_china['Recovered'].diff().fillna(0)
    df_china['new_Deaths'] = df_china['Deaths'].diff().fillna(0)
    df_china['p_new_Confirmed'] = df_china['new_Confirmed']/df_china['Confirmed']
    df_china['p_new_Recovered'] = df_china['new_Recovered']/df_china['Recovered']
    df_china['p_new_Deaths'] = df_china['new_Deaths']/df_china['Deaths']
    
    df_china.at[21, 'new_Confirmed']= 2022.0 # feb 12
    df_china.at[22, 'new_Confirmed']= 1820.0 # feb 13
    df_china.at[23, 'new_Confirmed']= 5093.0 # feb 14
    
    return {'italy':df_italy, 'china':df_china, 'usa':df_usa}
