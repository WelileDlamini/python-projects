# tuples
my_tuple = (1,2,3,4,5)
print(5 in my_tuple)
print(my_tuple[1])
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))

# sets
my_set = {1,2,3,4,5,5}# no duplicate
my_set.add(100)
my_set.add(2)
print(my_set)
print(1 in my_set)
print(len(my_set))
print(list(my_set))

# example
my_list = [1,2,3,4,5,5,5]
print(set(my_list))

# set methods
my_set = {1,2,3,4,5,}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set))
print(my_set.discard(5))
print(my_set.difference_update(your_set))
print(my_set.intersection(your_set))
print(my_set.isdisjoint(your_set))
print(my_set.issubset(your_set))
print(my_set.union(your_set))
print(my_set.issuperset(your_set))





