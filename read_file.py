fhandle = open('F:/downloads/romeo.txt','r')
lst = list()

for line in fhandle:
	words = line.split(' ')
	for word in words:
		if word not in lst:
			lst.append(word.strip())

fhandle.close()

lst.sort()
print lst
