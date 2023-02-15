# importing the requests library
import requests
import re
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning
from os import path
import yaml

# doc for API url : https://developer.vmware.com/apis/1083/nsx-t
url_list=[]
url_name = []
if path.exists('config.yml'):
    with open('config.yml', 'r') as config_file:
        try:
            config = yaml.safe_load(config_file)
            user = config['user']
            password = config['password']
            for URL in config['url_list']:
                url_list.append(URL['link'])
                url_name.append(URL['name'])
        except yaml.YAMLError as error:
            print(error)

def request_agent(URL):
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    # sending get request and saving the response as response object HTTPBasicAuth(user, password)
    r = requests.get(url=URL,auth=(user,password),verify=False )   
    # extracting data in json format
    data = r.json()      
    return data

def result_count_request():
    data_list = []
    for URL in url_list:
        data = request_agent(URL)
        data_list.append(data['result_count'])
    return data_list, url_list, url_name

