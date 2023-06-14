# exercise comprehensions
some_list = ['a','b','c','b','d','m','n','n']
duplicates = []
for value in some_list:
    if some_list.count(value)>1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

a = some_list.count(value)
print(a)


duplicates = set([value for value in some_list if some_list.count(value)>1])
print(duplicates)