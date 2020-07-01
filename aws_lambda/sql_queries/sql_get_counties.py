from sqlalchemy import create_engine
import pandas as pd
import mysql.connector
import psycopg2

engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres2.chtkfsooypac.us-east-1.rds.amazonaws.com:5432/postgres', echo=False)


def get_scraped_counties():
  sql = f'''
  SELECT * 
  FROM scraped_county_table;
  '''
  with engine.connect() as conn:
    return [record for record in conn.execute(sql)]

def get_historic_counties_records(): # all records before the scraped
  sql = f'''
  SELECT * 
  FROM historic_counties_table;
  '''
  with engine.connect() as conn:
    return [record for record in conn.execute(sql)]

def get_combined_counties():
  sql = f'''
  SELECT * 
  FROM combined_county_table;
  '''
  with engine.connect() as conn:
    return [record for record in conn.execute(sql)]
    
def get_historical_nyc_data():
  sql = f'''
  SELECT * 
  FROM historical_nyc_table;
  '''
  with engine.connect() as conn:
    return [record for record in conn.execute(sql)]
    
def get_combined_nyc_data():
  sql = f'''
  SELECT * 
  FROM combined_nyc_table;
  '''
  with engine.connect() as conn:
    return [record for record in conn.execute(sql)]


def get_historical_county_data():
    data = get_combined_counties()
    df_confirmed_historical_T = pd.DataFrame(data, columns=['Albany', 'Allegany', 'Bronx', 'Broome', 'Cattaraugus', 'Cayuga',
        'Chautauqua', 'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland',
        'Delaware', 'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton',
        'Genesee', 'Greene', 'Hamilton', 'Herkimer', 'Jefferson', 'Kings',
        'Lewis', 'Livingston', 'Madison', 'Manhattan', 'Monroe', 'Montgomery',
        'Nassau', 'New York', 'Niagara', 'Oneida', 'Onondaga', 'Ontario',
        'Orange', 'Orleans', 'Oswego', 'Otsego', 'Putnam', 'Queens',
        'Rensselaer', 'Richmond', 'Rockland', 'Saratoga', 'Schenectady',
        'Schoharie', 'Schuyler', 'Seneca','St. Lawrence',
        'Steuben', 'Suffolk', 'Sullivan', 'Tioga', 'Tompkins', 'Ulster',
        'Warren', 'Washington', 'Wayne', 'Westchester', 'Wyoming', 'Yates',
        'date', 'total'])
    df_confirmed_historical_T.reset_index(drop=True, inplace=True)
    return df_confirmed_historical_T