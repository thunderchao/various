from lxml import cssselect
from lxml import etree
from lxml import html
from urllib.parse import urlencode
import webbrowser

#This program scrapes a WorldCat list and then
#searches Google Scholar for each title. It
#also creates a unique text file containing
#the titles, authors, search URL, and citations.

def md(lexicon,key, contents):
    """Generic append key, contents to lexicon"""
    lexicon.setdefault(key,[]).append(contents)

user = input('WorldCat username? ')
wcln = input('WorldCat list number? ')

url = "http://www.worldcat.org/profiles/" + user + "/lists/" + wcln
tree = html.parse(url)
root = html.parse(url).getroot()
t = root.find_class('name')
a = root.find_class('author')

url2 = "http://www.worldcat.org/profiles/" + user + "/lists/" + wcln + "/bibliography?view=&style=TURABIAN&export=HTML&se=as&sd=asc&qt=sort_as_asc"
tree2 = html.parse(url2)
root2 = html.parse(url2).getroot()
c = root2.find_class('citation')

authors = [item.text_content()[3:] for item in a]
titles = [item.text_content() for item in t]
citations = [item.text_content() for item in c]

books = {}    
scholar_urls = {}
data = {'as_sdt':'1%2C5'} #leaves out patents
search_url = "http://scholar.google.com/scholar?"

for pair in zip(titles, authors):
    md(books, pair[0], pair[1])

##for title in titles:
##    data['q'] = title
##    url_data = urlencode(data)
##    full_url = search_url + url_data
##    md(scholar_urls, title, full_url)
##    webbrowser.open_new_tab(full_url)

with open(user + wcln + '.txt', encoding='utf-8', mode='w') as url_list:
    url_list.write("Worldcat list URL:\n\t" + url)
    url_list.write("Book Information and Google Scholar Search URLs\n\n")
    for k in scholar_urls:
        v = books[k]
        url_list.write(k + '\n' + str(v).strip("[']") + '\n' +
                       str(scholar_urls[k]) + '\n\n')
    url_list.write("List of Citations (Chicago)\n\n")
    for c in citations:
        url_list.write(c + '\n')

