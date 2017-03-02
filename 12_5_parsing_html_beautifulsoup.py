import urllib
from BeautifulSoup import *

html = urllib.urlopen('http://python-data.dr-chuck.net/known_by_Madison.html').read()

for i in range(7):
    soup = BeautifulSoup(html)
    tags = soup('a')
    new_url = tags[17].get('href', None)
    print new_url
    html = urllib.urlopen(new_url).read()
