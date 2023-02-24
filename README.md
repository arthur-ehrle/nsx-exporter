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
target : "https://NSX-Manager-IP:port" \
url_list : 
  - link : "/api/v1/logical-routers" \
    name : "logical_routers" 
  - link : "/api/v1/vpn/ipsec/dpd-profiles" \
    name : "dpd_profiles" 
  - link : "/policy/api/v1/infra/tier-1s" \
    name : "tier1_number" 
  - link : "/api/v1/edge-clusters" \
    name : "edge_clusters" 
  - link : "/policy/api/v1/infra/tier-0s" \
    name : "tier0_number" 
    
check_list:
  - link : "/policy/api/v1/infra/segments/" \
    name : "segment_down" \
    regex_word : "admin_state" \
    word: "DOWN"
  - link : "/policy/api/v1/infra/tier-0s/" \
    name : "tiers0_DOWN" \
    regex_word : "connectivity" \
    word: "OFF"


