# dictionay
dictionary = {
    'a': [1,2,3],
    'b':'hello',
    'x': True
}
print(dictionary['a'][1])
# or
my_list = [
    {
    'a': [1,2,3],
    'b':'hello',
    'x': True
    }
]
print(my_list[0]['a'][2])

# checking if a key is present
print(dictionary.get['get',55])

# alternative way to create dictionaries
user2 = dict(name='JohnJohn')
print(user2)
# dictionary methods
print('basket' in my_list)
print('hello' in my_list.values())
print(my_list.pop('x'))
print(my_list)
print(my_list.update({'age':55}))
print(my_list)