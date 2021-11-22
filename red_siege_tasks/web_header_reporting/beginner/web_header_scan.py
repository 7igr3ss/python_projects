#!/usr/bin/env python3

"""
PROJECT NAME: Web Header Reporting (Beginner)
VERSION: 1.0.0
AUTHOR: Empress O. Obazee (7igr3ss)
"""

# Imports
import argparse
import sys
import requests

# Banner
BANNER_INFO = f"================== Retrieving Web Headers =================="

# Creating ArugumentParser Arguments
EPL_INFO = "Queries the supplied urls for vulnerable web headers"
DESC_INFO = "API Key is needed from the xxx.xxxxx.xxxxx to run this script\n"

# Creating Arugument Parser Help Arguments
URL_INFO = "provide the URL link you wish to scan"
OUTPUT_INFO = "output result to a file"

# Arguments construction
PS_ARGS = argparse.ArgumentParser(description=f"{DESC_INFO}", 
                                epilog=f"{EPL_INFO}")
PS_ARGS.add_argument("-u", "--url", help=f"{URL_INFO}", dest="URL", required=True,
                            metavar="http(s)://xxxx.xxx", type=str)
PS_ARGS.add_argument("-o", "--output", help=f"{OUTPUT_INFO}", dest="OUTPUT",
                            metavar="/path/output.txt", type=str)
# Parse arguments
args = PS_ARGS.parse_args()

# Declaring Header
STS = "Strict-Transport-Security"

class WebHrScan:

    def __init__(self, URL=args.URL):
        self.url = URL
     
     
     # Query headers for a single url link
    def query_web_headers(self):
        data_entry = ""
        resp = requests.get(self.url)
        rsp_sts = resp.headers.get(STS)
        data_entry += BANNER_INFO
        data_entry += f"\nUrl: {self.url}"
        if rsp_sts is not None:
            data_entry += f"\n\t[✓] Strict-Transport-Security has been set!"
            data_entry += f"\n\t[!] Configured Setting(s): {rsp_sts}!"
        else:
            data_entry += f"\n\t[x] Strict-Transport-Security is missing!"
        return data_entry

        
# Output to file
def output_file(data_to_write, output_file=args.OUTPUT):
    with open(output_file, mode='w', encoding='utf-8') as output_results:
        output_results.write(data_to_write)
    print(f"[!] Results have been writen to - {output_file} file!")



if __name__ == '__main__':
    if args.URL is not None:
        if args.OUTPUT is not None:
            output_file(WebHrScan().query_web_headers())
        else:
             print(WebHrScan().query_web_headers())