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
        if headings[:5] == ['County', 'Confirmed', 'Deaths', 'Recoveries', 'Population','Deaths2Confirmed', 'Confirmed2Population']:
            break

    StringData = 'County; Confirmed; Deaths; Recoveries; Population; Deaths2Confirmed; Confirmed2Population \n'
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if not tds:
            continue
        try:
            county, confirmed, deaths, recoveries, population, death2confirmed, confirmed2pop= [td.text.strip() for td in tds[:7]]
            if '!' in county:
                county = county[country.index('!')+1:]
            county = re.sub('[^a-zA-Z ]+','',county)#for timeslider geojson matchup: [^a-zA-Z. ]+
            # print('; '.join([county, confirmed, deaths, recoveries, population, death2confirmed, confirmed2pop]))
            StringData += ('; '.join([county, confirmed, deaths, recoveries, population, death2confirmed, confirmed2pop]))+'\n'
        except ValueError:
            pass
    String = StringIO(StringData)
    df = pd.read_csv(String, sep =";") 
    df['lastupdate'] = datetime.now(tz=pytz.timezone('EST'))
    df['lastupdate'] = pd.to_datetime(df['lastupdate'], format = '%Y-%m-%d')
    df['lastupdate'] = df['lastupdate'].apply(lambda x: x.strftime('%B %d'))
    df = df.sort_values(by=' Confirmed', ascending=False)
    return df
