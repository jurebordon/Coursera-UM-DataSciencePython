#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#fhandler = open(name,'r')
fhandler = open('C:/Users/jureb/Documents/Dropbox/MyProjects/PythonCoursera/mbox-short.txt','r')
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