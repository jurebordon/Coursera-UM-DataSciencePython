import urllib
from BeautifulSoup import *
import re

urlhandler = urllib.urlopen('http://python-data.dr-chuck.net/comments_345847.html')

html = urlhandler.read()
soup = BeautifulSoup(html)

tags = soup('span')

sum = 0

for tag in tags:
	sum = sum + int(tag.contents[0])

print sum
