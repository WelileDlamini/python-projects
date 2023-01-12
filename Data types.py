# # boolean
# my_bool = True
# print(type(my_bool))
#
# # integers
# my_int = 32
# print(type(my_int))
#
# my_int = int(32)
# print(type(my_int))
#
# # float
# my_float = 34.6
# print(type(my_float))
#
# my_float = float(34.6)
# print(type(my_float))
# # complex
# my_complex_number = 32 + 4j
# print(type(my_complex_number))
#
# my_complex_number = complex(32 + 4j)
# print(type(my_complex_number))
#
# # string
# my_city = 'New York'
# print(type(my_city))
#
# my_city = str('New York')
# print(type(my_city))
# print(len('New York'))
# print('New York'.replace('New', 'Old'))
# # upper()
# print('New York'.upper())
# # lower
# print('New York'.lower())
#
# # lists
# my_list = ['bmw', 'ferrari', 'maclaren']
# print(type(my_list))
# my_list = list(('bmw', 'ferrari', 'maclaren'))
# print(type(my_list))
#
# # tuples
# my_tuple = ('bmw', 'volvo', 'toyota')
# print(type)(my_tuple)
# my_tuple = tuple(('bmw', 'volvo', 'toyota'))
# print(type(my_tuple))
#
# # sets
# my_set = {"bmw", "ferrari", "maclaren"}
# print(type(my_set))
# my_set = set(("bmw", "ferrari", "maclaren"))
# print(type(my_set))
#
# # dictionaries
# my_dict = {"country" : "France", "worldcups" : 2}
# print(type(my_dict))
# my_dict = dict(country ='France', worldcups=2)
# print(type(my_dict))

# typecasting
# this is just a regular explicit intialization
# my_str = str('32')
# print(my_str)
# int to string
# my_str = str(32)
# print(my_str)
# float to str
# my_str = str(32.0)
# print(my_str)
#
# # implicit conversion
# my_int = 32
# my_float = 3.2
# my_sum = my_int + my_float
# print(my_sum)
# print(type(my_sum))
#
# my_str = '34'
# my_int = 34
# my_sum = int(my_str) + my_int
# print(my_sum)
# # implicit conversion throws an error
# my_sum = my_int + my_str
# # the same error will be thrown when you try to add a float to a string
# my_sum = my_str + my_float

# user input function
# country = input('What is your country?')
# print(country)

age = input('How old are you?')
print(type(age))
age = int(age)
print(age)