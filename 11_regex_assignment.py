import re

fh = open("C:/Users/jureb/Documents/Dropbox/MyProjects/PythonCoursera/11_regex_sum_42.txt")

text_test = fh.read()

numbers_test = re.findall("[0-9]+", text_test)
print sum(map(int, numbers_test))

fh.close()

fh = open("C:/Users/jureb/Documents/Dropbox/MyProjects/PythonCoursera/11_regex_sum_345842.txt")

text = fh.read()

numbers = re.findall("[0-9]+", text)
print sum(map(int, numbers))
