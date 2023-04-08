# list
name = ['John', 'Bob', 'Mosh', 'Sarah']
name[0] = 'Jon'
print(name)

# challenge
numbers = [1,2,3,8,11,15,30]
max = numbers[0]
for item in numbers:
    if item > max:
        max = item
print(max)

# 2 Dimensional Lists
matrix = [
    [1,2,3]
    [4,5,6]
    [7,8,9]
]
matrix[0][1] = 20
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)
# list functions
numbers = [5,2,1,7,4,5]
numbers.append(20) # adding something on a list new
numbers.insert(0, 10) # inserting or replacing
numbers.remove(5) # removes a chracter in the list
numbers.clear() # removes everything
numbers.pop() # removes the last character in the list
numbers.index(5) # checking the index of a item in the list
print(5 in numbers)# boolean value either true or false
print(numbers)# boolean value either true or false
numbers.sort()#sorts numbers in accending order
numbers.reverse()# reverses the list whether sorted or not
numbers2 = numbers.copy()
print(numbers)
print(numbers.count(5))

# challenge that removes duplicates in a list
my_list = [1,1,3,3,5,5,7,7,8,8,10,10]
my_list = list(set(my_list))
print(my_list)

# another list
numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
#Tuples
numbers = (1,2,3)
print(numbers[0])

# unpacking
coordinates = (1,2,3)
# x = coordinates[0]
# y = coordinates [1]
# z = coordinates [2]
x,y,z = coordinates

# dictionaries
customer = {
    "name": "Jone Smith"
    "age" "30"
    "is_verified": True
}

