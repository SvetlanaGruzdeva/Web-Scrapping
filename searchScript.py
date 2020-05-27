import webbrowser
from googlesearch import search

query = input()

print('Searching...\n')
for searchResult in search(query, tld='com', lang='en', num=5, start=0, stop=5, pause=2):
    print(searchResult)
    webbrowser.open(searchResult)

print('\n' + 'Done!')