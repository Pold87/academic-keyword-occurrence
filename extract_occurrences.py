#!/usr/bin/env python
# By: Volker Strobel
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, build_opener, HTTPCookieProcessor
from http.cookiejar import LWPCookieJar
import re
import time
import sys

cookies = LWPCookieJar('./cookies')
try:
    cookies.load()
except IOError:
    pass

def get_num_results(search_term, start_date, end_date):
    """
    Helper method, sends HTTP request and returns response payload.
    """

    # Open website and read html
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
    query_params = { 'q' : search_term, 'as_ylo' : start_date, 'as_yhi' : end_date}
    url = "https://scholar.google.com/scholar?as_vis=1&hl=en&as_sdt=1,5&" + urllib.parse.urlencode(query_params)
    opener = build_opener(HTTPCookieProcessor(cookies))
    request = Request(url=url, headers={'User-Agent': user_agent})
    handler = opener.open(request)
    html = handler.read() 

    # Create soup for parsing HTML and extracting the relevant information
    soup = BeautifulSoup(html, 'html.parser')
    div_results = soup.find("div", {"id": "gs_ab_md"}) # find line 'About x results (y sec)

    if div_results != None:
        res = re.findall(r'(\d+),?(\d+)?,?(\d+)?\s', div_results.text) # extract number of search results
        if not res:
            num_results = '0'
        else:
            num_results = ''.join(res[0]) # convert string to number

        success = True
    else:
        success = False
        num_results = 0

    return num_results, success


def get_range(search_term, start_date, end_date, output_file="out.csv"):

    try:
        fp = open(output_file, 'w')
    except IOError:
        fp = open(output_file, 'w+')
    fp.write("year,results\n")
    print("year,results")

    for date in range(start_date, end_date + 1):

        num_results, success = get_num_results(search_term, date, date)
        if not(success):
            print("It seems that you made too many requests to Google Scholar. Please wait a couple of hours and try again.")
            break
        year_results = "{0},{1}".format(date, num_results)
        print(year_results)
        fp.write(year_results + '\n')
        time.sleep(0.8)

    fp.close()

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("******")
        print("Academic word relevance")
        print("******")
        print("")
        print("Usage: python extract_occurrences.py '<search term>' <start date> <end date> ['<output_file>']")

    else:
        try:
            search_term = sys.argv[1]
            start_date = int(sys.argv[2])
            end_date = int(sys.argv[3])
            if len(sys.argv) > 4:
                output_file = sys.argv[4]
                get_range(search_term, start_date, end_date, output_file)
            else:
                get_range(search_term, start_date, end_date)
        finally:
            cookies.save()
