# pure function
def multiply(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list
print(multiply([1,2,3,4]))

# map, filter,zip and reduce
# map allows us to simplify the code
def multiply(item):
   return item*2
print(list(map(multiply, [1,2,3,4]))) # data that gets acted upon

# filter
def multiply(item):
   return item*2

def check_odd(item):
    return item % 2 !=0
print(list(filter(check_odd, [1,2,3,4])))
# zip
my_list = [1,2,3]
your_list = [10,20,30]
def multiply(item):
   return item*2
def check_odd(item):
    return item % 2 !=0
print(list(zip(my_list, your_list)))

# reduced
from functools import reduce
my_list = [1,2,3]
def multiply(item):
   return item*2

def check_odd(item):
    return item % 2 !=0

def accumulator(acc, item):
    print(acc,item)
    return acc + item

print((reduce(accumulator,my_list,0)))