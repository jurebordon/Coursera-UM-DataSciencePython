#fname = raw_input("Enter file name: ")
#fhandler = open(fname, 'r')
fhandler = open('C:/Users/jureb/Documents/Dropbox/MyProjects/PythonCoursera/mbox-short.txt','r')
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