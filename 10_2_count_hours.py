import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'files/mbox-short.txt')

fhandler = open(filename)
counts = dict()

top_commiter = None
num_of_commits = None

for line in fhandler:
	if line.startswith("From "):
		words = line.split()
		# words[5] = time
		time = words[5].split(':')
		counts[time[0]] = counts.get(time[0],0) + 1

sorted_lst = sorted(counts.items())

for k,v in sorted_lst:
	print k,v

print "Execute for Python Coursera course!"