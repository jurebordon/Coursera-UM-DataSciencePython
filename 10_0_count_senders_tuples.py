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
		counts[words[1]] = counts.get(words[1],0) + 1
		if (counts[words[1]] > num_of_commits):
			top_commiter = words[1]
			num_of_commits = counts[words[1]]	

print top_commiter, num_of_commits
print '----'

lst = list()
for k,v in counts.items():
	lst.append( (v,k) )

lst.sort(reverse=True)

for val,key in lst[:5]:
	print key, val

lst2 = sorted([(v,k) for k,v in counts.items() ])

x,y = 3,4

print y

x= { 'chuck' : 1, 'fred':2}
y = x.items()
print type(y)