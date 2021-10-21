#!/usr/bin/env python3

print("""
\033[1;36;40m
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
PROJECT NAME: ipGeolocation for IPs in a list
VERSION: 1.0.1
AUTHOR: Empress O. Obazee (7igr3ss)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
\033[0m
""")

print("""

\033[1;36;40m###################################### IPGEOLOCATION SCRIPT ###################################### \033[0m
    
""")

# Imports
import requests
import sys
from datetime import datetime

# Variables
current = datetime.now()
dt_str = current.strftime("%d/%m/%Y %H:%M:%S")

# Usage
def help():
    print("Usage: ./ipGeolocation.py <ip address> <api_key>")
    print("Example: ./ipGeolocation.py 192.253.12.5 f2fb2bd77bab4b27ac702b0e363277e2")
    exit(0)

# IP query
def ipQuery(ipAddress, api_Key):
    data = {'ip' : ipAddress, 'apiKey' : api_Key}
    reqs = requests.get("https://api.ipgeolocation.io/ipgeo", params=data)
    
    # Data in json
    json_data = reqs.json()

    # Printing out the data
    ipaddr = json_data['ip']
    organization = json_data['organization']
    countryCode = json_data['country_code3']
    country = json_data['country_name']
    print(f"\033[1;33;40m[✓] [{dt_str}] ~ Quering IP ~ \033[0m")
    print(f"\tIP Address: {ipaddr}\r\n\tOrganization: {organization}\r\n\tCountry: {country}\r\n\tCountry Code: {countryCode}")

try:
    if len(sys.argv) != 3:
        help()
        sys.exit(0)

    if len(sys.argv) == 3:
        ipQuery(sys.argv[1], sys.argv[2])
except KeyError:
    print("[X] Please read the usage instructions carefully!")
    help()
    sys.exit(0)
