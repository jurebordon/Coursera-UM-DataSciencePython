import re

fh = open('C:/Users/jureb/Documents/Dropbox/MyProjects/PythonCoursera/mbox-short.txt','r')

text = fh.read()

for line in fh:
	line = line.rstrip()
	if re.search('^X-\S+',line):
		print line


x = "My 2 favorite numbers are 19 and 42"
y = re.findall('[0-9]+',x) # returns python list
print y

y = re.findall('[M]+\S', x)
print y

x = "From: Using the : character"
y = re.findall('^F.+:',x) #greedy, takes biggest
print y

x = "From: Using the : character"
y = re.findall('^F.+?:',x) #non - greedy, takes first matching
print y

#print text
y = re.findall('From (\S+@\S+)', text) # Find all emails
print y

y = re.findall('From \S+@(\S+)', text)
print y

y = re.findall('X-DSPAM-Confidence: ([0-9.]+)',text)
print max(y)


