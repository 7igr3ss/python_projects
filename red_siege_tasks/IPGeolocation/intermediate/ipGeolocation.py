#!/usr/bin/env python3


"""
PROJECT NAME: ipGeolocation for IPs in a list (Intermediate)
VERSION: 1.0.0
AUTHOR: Empress O. Obazee (7igr3ss)
COPYRIGHT © 2021 Empress Obazee
"""

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

# Help usage
def help():
    print("Usage: ./ipGeolocation.py </path/file> <api_key>")
    print("Example: ./ipGeolocation.py /path/ipaddress_list.txt f2fb2bd77bab4b27ac702b0e363277e2")
    exit(0)

# IP query
def ipQueryList(path2File, api_Key):
    try:
        # Read file from lists
        with open (path2File, mode='r', encoding='utf-8') as file:
            for ip_lists in file:
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
        ipQueryList(sys.argv[1], sys.argv[2])

except KeyError:
    print("[x] Please supply the right API Key!")