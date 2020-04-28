from bs4 import BeautifulSoup
from datetime import datetime
from io import StringIO 
import pandas as pd
import requests
import pytz
import re

def scrape_counties_wikipedia():
    website_url = requests.get('https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_New_York_(state)').text
    soup = BeautifulSoup(website_url,'lxml')
    tables = soup.find_all('table', class_='sortable')

    for table in tables:
        ths = table.find_all('th')
        headings = [th.text.strip() for th in ths]
        if headings[:7] == ['County', 'Confirmed', 'Deaths', 'Recoveries', 'Population']:
            break

    StringData = 'County; Confirmed; Deaths; Recoveries; Population;'
    StringData += '\n'
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if not tds:
            continue
        try:
            county, confirmed, deaths, recoveries, population= [td.text.strip() for td in tds[:7]]
            if '!' in county:
                county = county[county.index('!')+1:]
            county = re.sub('[^a-zA-Z ]+','',county)#for timeslider geojson matchup: [^a-zA-Z. ]+
            # print('; '.join([county, confirmed, deaths, recoveries, population, death2confirmed, confirmed2pop]))
            StringData += ('; '.join([county, confirmed, deaths, recoveries, population]))+'\n'
        except ValueError:
            pass
    String = StringIO(StringData)
    # StringData
    df = pd.read_csv(String, sep =";") 
    
    df.drop(columns='Unnamed: 5', inplace=True)
    df['lastupdate'] = datetime.now(tz=pytz.timezone('EST'))
    # df['lastupdate'] = pd.to_datetime(df['lastupdate'], format = '%Y-%m-%d')
    df['lastupdate'] = df['lastupdate'].apply(lambda x: x.strftime('%B %d %H:%M' ))
    collist = [' Confirmed', ' Deaths', ' Recoveries', ' Population']
    for i in collist:
        df[i] = df[i].str.replace(' ', '')
        df[i] = df[i].str.replace(',', '')
        df[i] = df[i].fillna(0)
        df[i] = df[i].astype('int')
    # df[collist] = df[collist].apply(pd.to_numeric, errors='coerce')#could not use this because need to remove commas
    df = df.sort_values(by=[' Confirmed'], ascending=False)
    df['County'] = df['County'].str.replace('New York City a', 'New York City')
    return df