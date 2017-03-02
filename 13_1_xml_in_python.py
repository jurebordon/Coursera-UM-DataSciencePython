import xml.etree.ElementTree as ET
import urllib

#url = raw_input('Enter url: ')

url = ' http://python-data.dr-chuck.net/comments_345844.xml'

print 'Retrieving', url

uh = urllib.urlopen(url)
data = uh.read()

print 'Retrieved',len(data),'characters'

stuff = ET.fromstring(data)
counts = stuff.findall('comments/comment/count')
print 'Counts count:', len(counts)

sum = 0

for count in counts:
    sum = sum + int(count.text)

print "Sum: ", Sum