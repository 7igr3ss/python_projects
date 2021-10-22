#!/usr/bin/env python3

print("""
\033[1;36;40m
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
PROJECT NAME: ipGeolocation for IPs in a list
VERSION: 1.0.0
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
import ipaddress
from datetime import datetime

# Variables
current = datetime.now()
dt_str = current.strftime("%d/%m/%Y %H:%M:%S")

# Usage
def help():
    print("Usage: ./ipGeolocation.py </path/file> <api_key>")
    print("Example: ./ipGeolocation.py /path/ipaddress_list.txt f2fb2bd77bab4b27ac702b0e363277e2")
    exit(0)

# CIDR IPv4 Query
def cidrIpQuery(path2File, api_Key):
    try:
        with open (path2File, mode='r') as file:
            contents = file.readlines()
            for entry in contents:
                sp = entry.replace("\n","").replace("\r","")
                cidr = ipaddress.ip_network(sp)
                for ip_lists in cidr.hosts():
                    data = {'ip' : ip_lists, 'apiKey' : api_Key}
                    reqs = requests.get("https://api.ipgeolocation.io/ipgeo", params=data)

                    # Data in json
                    json_data = reqs.json()

                    # Printing out the data
                    ipaddr = json_data['ip']
                    organization = json_data['organization']
                    countryCode = json_data['country_code3']
                    country = json_data['country_name']
                    print(f"\n \033[1;33;40m[✓] [{dt_str}] ~ Quering IP in List ~ \033[0m")
                    print(f"\tIP Address: {ipaddr}\r\n\tOrganization: {organization}\r\n\tCountry: {country}\r\n\tCountry Code: {countryCode}")
    except (IsADirectoryError, FileNotFoundError) as e:
        print("[x] Please enter the correct path to file that contains your IP Addresses!")

try:
    if len(sys.argv) != 3:
        help()
        sys.exit(0)

    if len(sys.argv) == 3:
        cidrIpQuery(sys.argv[1], sys.argv[2])

except KeyError:
    print("[x] Please supply the right API Key!")