from sqlalchemy import create_engine
import mysql.connector
import pandas as pd
import psycopg2
#Local Imports
from scrape.scrape_counties import scrape_counties_wikipedia


engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres2.chtkfsooypac.us-east-1.rds.amazonaws.com:5432/postgres', echo=False)

def execute_scrape_counties_wikipedia():
    df = scrape_counties_wikipedia()
    df.to_sql(name='county_table', con=engine, index=False, if_exists="replace")
#if_exists options: {‘fail’, ‘replace’, ‘append’}, default ‘fail’
