from dotenv import load_dotenv
import os
import yaml

#load call config variables
with open("security_master/config/config.yaml") as f:
    #TODO: is there a better way to load this location?
    config = yaml.safe_load(f)

#Load all environment variables (highest available .env file)
load_dotenv() 

api_key = os.getenv("API_KEY")
base_url = config["api"]["base_url"]
fxiax_coverage_location = config["fxaix_covergae"]["file_location"]