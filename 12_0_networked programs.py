import socket
import urllib

# OLD WAYS - hacky stuff with GET requests

# mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysocket.connect(('www.py4inf.com',80))

# mysocket.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0 \n\n')

# while True:
# 	data = mysocket.recv(512)
# 	if(len(data)<1):
# 		break
# 	print data

# mysocket.close()

# With URLLIB library - much easier

urlhandler = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in urlhandler:
	print line.strip()