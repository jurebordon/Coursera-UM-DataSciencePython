#fname = raw_input("Enter file name: ")
#fhandler = open(fname, 'r')
fhandler = open('F:/downloads/mbox-short.txt','r')

cnt = 0

for line in fhandler:
	if line.startswith("From "):
		words = line.split()
		print words[1]
		cnt = cnt + 1

print "There were", cnt, "lines in the file with From as the first word"