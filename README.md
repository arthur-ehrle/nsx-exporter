# Nsx-exporter
An open-source prometheus exporter for nsx-T 3.x.x

# Utilisation
Exporter is exposing metrics at : http://localhost:7789/
You can change the port in the YAML file.
There is some metrics about the python process itslef, but the most importants metrics are tagged by "NSXv3" at the begining.

# Config.yml

port: 7789
scrape_frequency: 1
user : ""
password : ""
label : "NSXv3"
url_list : 
  - link : "https://ip/api/v1/logical-routers"
    name : "logical-routers"
  - link : "https://ip/api/v1/vpn/ipsec/dpd-profiles"
    name : "dpd-profiles"
  - link : "https://ip/policy/api/v1/infra/tier-1s"
    name : "tier1_number"
  - link : "https://ip/api/v1/edge-clusters"
    name : "edge-clusters"
