from collections import Counter, defaultdict, OrderedDict

list = [1,2,3,4,5,6,7,7]
sentence = 'blah blah blah thinking about python'
print(Counter(list))# gives out or prints out a dictionary
print(Counter(sentence))

# defaultdict
dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})# allows access to a key by giving a default value
print(dictionary['a'])
print(dictionary['c']) # give it a default value

# ordereddict, returns the order that you insert into a dictionary
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2
print(d2 == d)

# datetime module, allows you to manipulate day to day values
import datetime
print(datetime.time(5,45,2))
print(datetime.date.today())

# an array
from array import array

arr = array('i', [1,2,3])

print(arr[0])