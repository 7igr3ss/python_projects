#!/usr/bin/env python3

"""
PROJECT NAME: Web Header Reporting (mockup)
VERSION: 1.0.0
AUTHOR: Empress O. Obazee (7igr3ss)
COPYRIGHT © 2021 Empress Obazee
"""

# Imports
import argparse
import sys
import requests

# ASCII Colour Codes
BRIGHT_GREEN = "\033[1;32;40m"
BRIGHT_RED ="\033[1;31;40m"
YELLOW = "\033[1;33;40m"

# Banner
BANNER_INFO = f"{BRIGHT_GREEN}================== Retrieving Web Headers =================="

# Creating ArugumentParser Arguments
EPL_INFO = "Queries the supplied urls for vulnerable web headers"
DESC_INFO = "API Key is needed from the xxx.xxxxx.xxxxx to run this script\n"

# Creating Arugument Parser Help Arguments
URL_INFO = "provide the URL link you wish to scan"
URL_FILE_INFO = "supply the file/list that contains URL links you wish to scan"
OUTPUT_INFO = "output result to a file"

# Arguments construction
PS_ARGS = argparse.ArgumentParser(description=f"{DESC_INFO}", 
                                epilog=f"{EPL_INFO}")

GROUPS = PS_ARGS.add_mutually_exclusive_group(required=True)

GROUPS.add_argument("-u", "--url", help=f"{URL_INFO}", dest="URL",
                            metavar="http(s)://xxxx.xxx", type=str)
GROUPS.add_argument("-f", "--url_file", help=f"{URL_FILE_INFO}", dest="FILE",
                            metavar="/path/filelist.txt", type=str)
PS_ARGS.add_argument("-o", "--output", help=f"{OUTPUT_INFO}", dest="OUTPUT",
                            metavar="/path/output.txt", type=str)
# Parse arguments
args = PS_ARGS.parse_args()

# Declaring Headers
STS = "Strict-Transport-Security"
CSP = "Content-Security-Policy"
XFO = "X-Frame-Options"


class WebHrScan:

    # Initializing arguments
    def __init__(self, URL=args.URL, FILE=args.FILE, OUTPUT=args.OUTPUT, BANNER=BANNER_INFO):
        self.url = URL
        self.file = FILE
        self.output = OUTPUT
        self.banner = BANNER

    # Query headers for a single url link
    def query_web_headers(self):
        resp = requests.get(self.url)
        rsp_sts = resp.headers.get(STS)
        rsp_csp = resp.headers.get(CSP)
        rsp_xfo = resp.headers.get(XFO)
        print(BANNER_INFO)
        print(f"\n{BRIGHT_GREEN}Url: {self.url}")
        if rsp_sts is not None:
            print(f"\n\t{BRIGHT_GREEN}[✓] Strict-Transport-Security has been set!")
            print(f"\t{YELLOW}[!] Configured Setting(s): {rsp_sts}!")
        if rsp_sts is None:
            print(f"\n\t{BRIGHT_RED}[x] Strict-Transport-Security is missing!")
        if rsp_csp is not None:
            print(f"\n\t{BRIGHT_GREEN}[✓] Content-Security-Policy has been set!")
            print(f"\t{YELLOW}[!] Configured Setting(s): {rsp_csp}!")  
        if rsp_csp is None:
            print(f"\n\t{BRIGHT_RED}[x] Content-Security-Policy is missing!")    
        if rsp_xfo is not None:
            print(f"\n\t{BRIGHT_GREEN}[✓] X-Frame-Options has been set!")
            print(f"\t{YELLOW}[!] Configured Setting(s): {rsp_xfo}!")
        if rsp_xfo is None:
            print(f"\n\t{BRIGHT_RED}[x] X-Frame-Options is missing!")
               

    # Query headers for multiple url links from a file
    def query_file(self):
        with open(self.file, mode='r', encoding='utf-8') as read_links:
            print(BANNER_INFO)
            for links in read_links:
                rem_space = links.replace("\n","").replace("\r","")
                resp = requests.get(rem_space)
                rsp_sts = resp.headers.get(STS)
                rsp_csp = resp.headers.get(CSP)
                rsp_xfo = resp.headers.get(XFO)
                print(f"\n{BRIGHT_GREEN}Url: {links}")
                if rsp_sts is not None:
                    print(f"\n\t{BRIGHT_GREEN}[✓] Strict-Transport-Security has been set!")
                    print(f"\t{YELLOW}[!] Configured Setting(s): {rsp_sts}!")
                if rsp_sts is None:
                    print(f"\n\t{BRIGHT_RED}[x] Strict-Transport-Security is missing!")
                if rsp_csp is not None:
                    print(f"\n\t{BRIGHT_GREEN}[✓] Content-Security-Policy has been set!")
                    print(f"\t{YELLOW}[!] Configured Setting(s): {rsp_csp}!")  
                if rsp_csp is None:
                    print(f"\n\t{BRIGHT_RED}[x] Content-Security-Policy is missing!")    
                if rsp_xfo is not None:
                    print(f"\n\t{BRIGHT_GREEN}[✓] X-Frame-Options has been set!")
                    print(f"\t{YELLOW}[!] Configured Setting(s): {rsp_xfo}!")
                if rsp_xfo is None:
                    print(f"\n\t{BRIGHT_RED}[x] X-Frame-Options is missing!")


if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            PS_ARGS.print_help()
        elif args.URL is not None:
            WebHrScan().query_web_headers()
        elif args.FILE is not None:
            WebHrScan().query_file()
    except:
        PS_ARGS.print_help()
