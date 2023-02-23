# importing the requests library
import requests
import re
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning
from os import path
import yaml
from nested_lookup import nested_lookup

# doc for API url : https://developer.vmware.com/apis/1083/nsx-t
url_list=[]
url_name = []
ListStateToCheck=[]
NameToCheck=[]
WordToCheck=[]
RegexWord=[]
if path.exists('config/config.yml'):
    with open('config/config.yml', 'r') as config_file:
        try:
            config = yaml.safe_load(config_file)
            user = config['user']
            password = config['password']
            for URL in config['url_list']:
                url_list.append(URL['link'])
                url_name.append(URL['name'])
            for URL in config['check_list']:
                ListStateToCheck.append(URL['link'])
                NameToCheck.append(URL['name'])
                WordToCheck.append(URL['word'])
                RegexWord.append(URL['regex_word'])
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

def connectivity_state():
   
    ValueList = []
    NameList = []
    render=[]
    renderAggreg=[]
    for URL in ListStateToCheck:
        index = ListStateToCheck.index(URL)
        word=WordToCheck[index]
        data = request_agent(URL)
        ValueList=nested_lookup(RegexWord[index], data)
        NameList = nested_lookup('display_name', data)
        render = match_name_state(ValueList,NameList,word,NameToCheck[index]) 
        renderAggreg.append(render)
    return renderAggreg

def match_name_state(list1,list2,word,name):
    render=[]
    for element in list1:
        index = list1.index(element)
        if element == word:
            render.append(list2[index])
    return render,name

