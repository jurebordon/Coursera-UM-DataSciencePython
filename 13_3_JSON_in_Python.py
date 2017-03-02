import json
import urllib

url = "http://python-data.dr-chuck.net/comments_345848.json"

print 'Retrieving', url

uh = urllib.urlopen(url)
data = uh.read()

print 'Retrieved',len(data),'characters'

stuffs = json.loads(data)

sum = 0

for stuff in stuffs["comments"]:
	#print stuff["count"]
	sum = sum + stuff["count"]

print sum