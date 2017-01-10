import urllib
import re

urlhandler = urllib.urlopen('http://python-data.dr-chuck.net/comments_345847.html')

html = urlhandler.read()
print html

numbers = map(int, re.findall('<span[^0-9]+(\d+)',html))

print sum(numbers)