import re
import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'files/11_regex_sum_42.txt')


fh = open(filename)

text_test = fh.read()

numbers_test = re.findall("[0-9]+", text_test)
print sum(map(int, numbers_test))

fh.close()

filename = os.path.join(dir, 'files/11_regex_sum_345842.txt')
fh = open(filename)

text = fh.read()

numbers = re.findall("[0-9]+", text)
print sum(map(int, numbers))
