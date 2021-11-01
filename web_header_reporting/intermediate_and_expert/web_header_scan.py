#!/usr/bin/env python3

"""
PROJECT NAME: Web Header Reporting
VERSION: 1.0.0
AUTHOR: Empress O. Obazee (7igr3ss)
COPYRIGHT © 2021 Empress Obazee
[Work in progress]
"""

# Imports
import argparse
import requests

# Banner
BANNER_INFO = "================== Retrieving Web Headers =================="

# Creating ArugumentParser Arguments
EPL_INFO = "Queries the supplied urls for vulnerable web headers"
DESC_INFO = ""

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
    def __init__(self, URL=args.URL, FILE=args.FILE, OUTPUT=args.OUTPUT):
        self.url = URL
        self.file = FILE
        self.output = OUTPUT

    # Query headers for a single url link
    def query_web_headers(self):
        data_entry = ""
        resp = requests.get(self.url)
        rsp_sts = resp.headers.get(STS)
        rsp_csp = resp.headers.get(CSP)
        rsp_xfo = resp.headers.get(XFO)
        print(BANNER_INFO)
        data_entry = f"\nUrl: {self.url}"
        if rsp_sts is not None:
            data_entry += f"\n\t[✓] Strict-Transport-Security has been set!"
            data_entry += f"\n\t[!] Configured Setting(s): {rsp_sts}!"
        else:
            data_entry += f"\n\t[x] Strict-Transport-Security is missing!"

        if rsp_csp is not None:
            data_entry += f"\n\t[✓] Content-Security-Policy has been set!"
            data_entry += f"\n\t[!] Configured Setting(s): {rsp_csp}!"
        else:
            data_entry += f"\n\t[x] Content-Security-Policy is missing!"

        if rsp_xfo is not None:
            data_entry += f"\n\t[✓] X-Frame-Options has been set!"
            data_entry += f"\n\t[!] Configured Setting(s): {rsp_xfo}!"
        else:
            data_entry += f"\n\t[x] X-Frame-Options is missing!"
        return data_entry
      

    # Query headers for multiple url links from a file
    def query_file(self):
        with open(self.file, mode='r', encoding='utf-8') as read_links:
            for links in read_links:
                rem_space = links.replace("\n","").replace("\r","")
                data_entry = ""
                resp = requests.get(rem_space)
                rsp_sts = resp.headers.get(STS)
                rsp_csp = resp.headers.get(CSP)
                rsp_xfo = resp.headers.get(XFO)
                data_entry += BANNER_INFO
                data_entry += f"\nUrl: {links}"
                if rsp_sts is not None:
                    data_entry += f"\n\t[✓] Strict-Transport-Security has been set!"
                    data_entry += f"\n\t[!] Configured Setting(s): {rsp_sts}!"
                else:
                    data_entry += f"\n\t[x] Strict-Transport-Security is missing!"

                if rsp_csp is not None:
                    data_entry += f"\n\t[✓] Content-Security-Policy has been set!"
                    data_entry += f"\n\t[!] Configured Setting(s): {rsp_csp}!"
                else:
                    data_entry += f"\n\t[x] Content-Security-Policy is missing!"

                if rsp_xfo is not None:
                    data_entry += f"\n\t[✓] X-Frame-Options has been set!"
                    data_entry += f"\n\t[!] Configured Setting(s): {rsp_xfo}!"
                else:
                    data_entry += f"\n\t[x] X-Frame-Options is missing!"
                return data_entry

# Output to file
def output_file(data_to_write, output_file=args.OUTPUT):
    with open(output_file, mode='a', encoding='utf-8') as output_results:
        output_results.write(data_to_write)
    print(f"[!] Results have been writen to - {output_file} file!")


if __name__ == '__main__':
    if args.URL is not None:
        if args.OUTPUT is not None:
            output_file(WebHrScan().query_web_headers())
        else:
            print(WebHrScan().query_web_headers())

    if args.FILE is not None:
        if args.OUTPUT is not None:
            output_file(WebHrScan().query_file())
        else:
            print(WebHrScan().query_file())