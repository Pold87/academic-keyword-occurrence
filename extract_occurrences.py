# By: Volker Strobel, improved by Patrick Hofmann
from bs4 import BeautifulSoup
from urllib.request import Request, build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import MozillaCookieJar
import re
import time
import sys
import urllib
import csv


def get_num_results(search_term):
    """
    Helper method, sends HTTP request and returns response payload.
    """

    # Open website and read html
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
    query_params = {'q': search_term}
    url = "https://scholar.google.com/scholar?as_vis=1&hl=en&as_sdt=1,5&" + \
        urllib.parse.urlencode(query_params)
    opener = build_opener()
    request = Request(url=url, headers={'User-Agent': user_agent})
    handler = opener.open(request)
    html = handler.read()

    # Create soup for parsing HTML and extracting the relevant information
    soup = BeautifulSoup(html, 'html.parser')
    # find line 'About x results (y sec)
    div_results = soup.find("div", {"id": "gs_ab_md"})

    if div_results != None:

        # extract number of search results
        res = re.findall(r'(\d+).?(\d+)?.?(\d+)?\s', div_results.text)

        if res == []:
            num_results = '0'
            success = True
        else:
            num_results = ''.join(res[0])  # convert string to number
            success = True

    else:
        success = False
        num_results = 0

    return num_results, success


def get_range(reader):

    fp = open("out.csv", 'w')
    fp.write("search_term,results\n")
    print("search_term, results")

    for row in reader:
        search_term = row[0]
        num_results, success = get_num_results(search_term)
        if not(success):
            print("It seems that you made to many requests to Google Scholar. Please wait a couple of hours and try again.")
            break
        search_term_results = "{0},{1}".format(search_term, num_results)
        print(search_term_results)
        fp.write(search_term_results + '\n')
        time.sleep(1.1)

    fp.close()
    
if __name__ == "__main__":
    print("******")
    print("Academic word relevance")
    print("******")
    print("")
    print("Usage: python extract_occurences.py")

    with open("input.csv", mode='r') as file:
        reader = csv.reader(file)
        get_range(reader)
