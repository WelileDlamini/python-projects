# lambda expression
from functools import reduce
my_list = [1,2,3]

print(list(map(lambda item: item*2 ,my_list)))
print(list(filter(lambda item: item % 2 !=0,my_list)))
print(reduce(lambda acc, item: acc + item ,my_list))

# # lambda expression exercises
# square
my_list = [5,4,3]
print(list(map(lambda item: item**2,my_list)))

# list sorting
a =[(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x: x[1])
print(a)

# list,sets comprehensions
my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)

#
my_list = [char for char in 'hello']

my_list2 = [num for num in range(0,100)]
my_list3 = [num*3 for num in range(0,100)]
my_list4 = [num **3 for num in range(0,100) if num%2==0 ]
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# set and dictionary comprehensions
my_list2 = {num for num in range(0,100)}
my_list3 = {num*3 for num in range(0,100)}
my_list4 = {num **3 for num in range(0,100) if num%2==0 }
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

#dictionary comprehensions
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k:v**2 for k,v in simple_dict.items() if v%2==0}
print(my_dict)


# exercise comprehensions
some_list = ['a','b','c','b','d','m','n','n']
duplicates = []
for value in some_list:
    if some_list.count(value)>1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)


print()

