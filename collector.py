import time
import random
import requests
from os import path
import yaml
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
import api

class result_count_request(object):
    def __init__(self):
        pass
    def collect(self):
        data_list, url_list, url_name = api.result_count_request()
        try:
            for URL in url_list:
                index = url_list.index(URL)
                gauge = GaugeMetricFamily(f"{label}_{url_name[index]}", f"{url_name[index]}", labels=[f"{url_name[index]}"])
                val = int(data_list[index])
                gauge.add_metric([f'{url_name[index]}'], data_list[index])
                yield gauge
        except:
            print(f"Failed to join the destination or error in the API result \n Result of the request : \n*data_list: {data_list} \n*url_list: {url_list} \n*url_name: {url_name}")
        
class match_request(object):
    def __init__(self):
        pass
    def collect(self):
        renderAggreg=api.connectivity_state()
        try:
            for MatchList,NameInList in renderAggreg:
                for siteDown in MatchList:
                    index = MatchList.index(siteDown)
                    gauge = GaugeMetricFamily(f"{label}_{NameInList}", f"{label}_{NameInList}", labels=[f"{NameInList}"])
                    val = 1
                    gauge.add_metric([f'{siteDown}'], val)
                    yield gauge
        except:
            print(f"Failed to join the destination or error in the API result \n Result of the request : \n*renderAggreg: {renderAggreg} ")
            
if __name__ == "__main__":
    if path.exists('config/config.yml'):
        print("Config file loaded correctly ")
        with open('config/config.yml', 'r') as config_file:
            try:
                config = yaml.safe_load(config_file)
                port = int(config['port'])
                frequency = config['scrape_frequency']
                label = config['label']
            except yaml.YAMLError as error:
                print(error)
    start_http_server(port)
    print(f"HTTP server started correctly on port {port}")
    REGISTRY.register(result_count_request())
    REGISTRY.register(match_request())
    while True: 
        # period between collection
        time.sleep(frequency)