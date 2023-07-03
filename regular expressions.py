import re

string = 'search inside of this text please'

a = re.search('inside', string)
print(a.span()) # gives a range of the index as a tuple
print(a.start()) # gives the start of the index where the text start

# or
import re

pattern = re.compile('this')
string = 'search this inside of this text please'
b = pattern.search(string)
c = pattern.findall(string)
d = pattern.fullmatch(string)
e = pattern.match(string)
print(b)
print(c)
print(d)
print(e)

# testing in python

