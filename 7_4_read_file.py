import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'files/romeo.txt')
fhandle = open(filename)
lst = list()

for line in fhandle:
	words = line.split(' ')
	for word in words:
		if word not in lst:
			lst.append(word.strip())

fhandle.close()

lst.sort()
print lst
