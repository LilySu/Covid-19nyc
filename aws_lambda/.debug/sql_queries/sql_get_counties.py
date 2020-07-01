from sqlalchemy import create_engine
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