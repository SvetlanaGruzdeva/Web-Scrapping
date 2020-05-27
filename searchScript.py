#! python3
# searchScript - Opens several search results.

import requests, sys, webbrowser, bs4
from pprint import pprint

print('Searching...') # display text while downloading the search result page
# res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res = requests.get('https://www.google.com/search?q=' + 'cat')
# print(res.text)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns wierd content, probably because of parser. Critically review.
# print(soup)

# Open a browser tab for each result.
linkElems = soup.select('p.LC20lb.DKV0Md')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://www.google.com' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
