from datetime import datetime, date, time, timedelta
from pytz import timezone

from wrangle.wrangle_counties import wrangle_sodapy_one_row_new_counties_data


def wrangle_check_update():
    """
    -Checks Datetime string of the 1 row county dataframe in wrangle_counties
    -Returns a string regarding if app needs an update or does not need an update
    """
    dft = wrangle_sodapy_one_row_new_counties_data()
    last_update = list(dft['date'])
    now = datetime.now(timezone('EST'))
    now = now.strftime('%B %d')
    status = 'Does Not Need Update'
    if now not in last_update:
        status = 'Needs Update'
    return status

