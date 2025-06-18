import requests
import config.loader as config
import pandas as pd

def get_currant_usage() -> int:
    """
    Retrieves the usage within the last minute.
    Note: Does not return total daily usage. MUST TRACK YOURSELF
    https://twelvedata.com/docs#api-usage

    returns (int) : api usage within the last minute 
    """
    usage_url = config.base_url + f'/api_usage?apikey={config.api_key}'
    r = requests.get(usage_url)
    if r.status_code == 200 and 'code' not in r.json():
        data = r.json()
        return data["current_usage"]
    else:
        if 'code' in r.json():
            raise Exception(r.json())
        else:
            r.raise_for_status()
    

def pull_security_master(stock_type='Common Stock', country='US'):
    """
    Pulls stock attribute data from twelvedata. 
    returns
    """
    sm_url = config.base_url + f"/stocks?apikey={config.api_key}&type={stock_type}&country={country}"
    r = requests.get(sm_url)
    if r.status_code == 200 and 'code' not in r.json():
        return r.json()["data"]
    else:
        if 'code' in r.json():
            raise Exception(r.json())
        else:
            r.raise_for_status()

def validate_fxiax_coverage():
    """
    Validates that the coverage in the FXIAX static symbol list is 
    """
    pass

def json_to_s3(json_response):
    """
    Takes a json response and writes it directly to s3
    """
    #TODO: Go over AWS login requirements 
    pass

def pull_FXIAX_coverage() -> list:
    """
    locally retrieves the FIAX coverage list from June 17th 
    """
    fxiax_df = pd.read_csv(config.fxiax_coverage_location)
    fxiax_tickers = fxiax_df["ticker"].to_list()
    return fxiax_tickers

#TODO - write a decorator to compare runtimes

def driver():
    #pull the security master from 12data and validate coverage
    security_master_json = pull_security_master()
    sp500_tickers = pull_FXIAX_coverage()
    validate_fxiax_coverage()

    
    


if __name__ == "__main__":
    driver()


