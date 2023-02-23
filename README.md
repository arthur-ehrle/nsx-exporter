# NSX-exporter
An open-source prometheus exporter for nsx-T 3.x.x

# Docker
Link to the docker image https://hub.docker.com/r/aehr/nsxv3-exporter

# Utilisation
Exporter is exposing metrics at : http://localhost:PortNumber/
You can change the port in the YAML file.
There is some metrics about the python process itslef, but the most importants metrics are tagged by "NSXv3" at the begining.

# Config.yml

port: 7789 \
scrape_frequency: 1 \
user : "login" \
password : "password!" \
label : "NSXv3" \
url_list : 
  - link : "https://Target_IP" \
    name : "" \
check_list: 
  - link : "https://Target_IP/policy/api/v1/infra/segments/" \
    name : "segment_down" \
    regex_word : "admin_state" \
    word: "DOWN" 
  - link : "https://Target_IP/policy/api/v1/infra/tier-0s/" \
    name : "tiers0_UP" \
    regex_word : "connectivity" \
    word: "OFF" 


