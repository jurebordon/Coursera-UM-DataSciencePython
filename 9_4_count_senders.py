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
		counts[words[1]] = counts.get(words[1],0) + 1
		if (counts[words[1]] > num_of_commits):
			top_commiter = words[1]
			num_of_commits = counts[words[1]]	

print top_commiter, num_of_commits