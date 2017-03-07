import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'files/mbox-short.txt')

fhandler = open(filename)

cnt = 0

for line in fhandler:
	if line.startswith("From "):
		words = line.split()
		print words[1]
		cnt = cnt + 1

print "There were", cnt, "lines in the file with From as the first word"