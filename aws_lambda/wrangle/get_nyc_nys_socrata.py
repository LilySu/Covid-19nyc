from sodapy import Socrata
import pandas as pd


def get_nys_data():
    """
    -Pulls all data from https://dev.socrata.com/foundry/health.data.ny.gov/xdss-u53e
    -Data is coming in with the earliest first if limit is set
    -Returns the first 62 corresponding to 62 counties

    """
    client = Socrata("health.data.ny.gov", None)
    results = client.get("xdss-u53e", limit=10000000)
    df = pd.DataFrame.from_records(results)
    df['test_date'] = pd.to_datetime(df['test_date'])
    
    latest_expected_date_of_update = datetime.now(timezone('EST'))-timedelta(days=1)
    latest_expected_date_of_update = latest_expected_date_of_update.strftime('%Y-%m-%d')
    
    df = df[df['test_date']==latest_expected_date_of_update]
    return df

