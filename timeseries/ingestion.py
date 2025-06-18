import requests
import config.loader as config


#Get the static list of fortune 500 companies
# Timeseries  Demo full history AAPL 2019
stock_url_history= config.base_url + "/time_series?apikey=demo&symbol=AAPL&interval=1day&start_date=2019-01-01"
r = requests.get(stock_url_history)
if r.status_code == 200 and 'code' not in r.json() == 200:
    print(r.json())
else:
    print(r.status_code)
    print(r.json())


def generate_timeseries_api_calls():
    """
    Creates the requests to be sent to the timeseries calls
    """
    #use multiprocessing here!
    pass

def pull_timeseries_data_concurrecntly():
    """
    Uses multiprocessing and coroutines to pull the latest timeseries
    """
    #use asyncio and 
    pass

def pull_timeseries_data_sequentially():
    """
    """
    pass

def driver():
    #pull timeseries based data and timeit
    pull_timeseries_data_concurrecntly()
    pull_timeseries_data_sequentially()