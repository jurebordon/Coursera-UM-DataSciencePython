import urllib
from BeautifulSoup import *

urlhandler = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in urlhandler:
	print line.strip()

# Soup
html = urllib.urlopen('http://www.dr-chuck.com').read()
soup = BeautifulSoup(html)
tags = soup('a')

for tag in tags:
	print tag.get('href', None)

