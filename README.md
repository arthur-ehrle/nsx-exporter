# NSX-exporter
An open-source prometheus exporter for nsx-T 3.x.x

# Docker
Link to the docker image https://hub.docker.com/r/aehr/nsxv3-exporter

# Utilisation
Exporter is exposing metrics at : http://localhost:PortNumber/
You can change the port in the YAML file.
There is some metrics about the python process itslef, but the most importants metrics are tagged by "NSXv3" at the begining.

# Config.yml

port: 7789
scrape_frequency: 1
user : ""
password : ""
label : "NSXv3"
url_list : 
  - link : "https://op-nsx-manager-dcf1.oncloud.host"
    name : ""
check_list:
  - link : "https://op-nsx-manager-dcf1.oncloud.host"
    name : ""
    word: "DOWN"
