# print("Welile")
# print("0----")
# print("|||")

# variables
price = 10
price = 20
print(price)

name = "Jonh Smith"
age = 20
is_new = True

name = input("What is your name? ")
color = input("What is your favourite color? ")
# print(f"{name} likes {color}")
print(name + "likes" + color)

# type conversion
birth_year = int(input("Birth year: "))
print(type(birth_year))
age = 2023 - birth_year
print(type(age))


# user weight
weight_in_pounds = int(input("What is your weight? "))
weight_in_kilos = weight_in_pounds*0.45
print(weight_in_kilos)

# strings
course = "Python course for Beginners"
another = course[:]
print(another)

# exercise
name = "Jenifer"
print(name[1:-1])

# formatted strings
first = "John"
last = "Smith"
# massage = first + '[' + last + '] is a coder '
msg = f'{first} [{last}] is a coder'
print(massage)

# string methods
course = "Python for Beginners"
print(len(course))
course.upper()
print(course.find('P'))
print(course.replace('Beginners', 'Absolute Beginners'))
print("Python" in course)
course.upper()
course.lower()
course.title()

# Arithmetic operations
x = 10
x = x + 3
x += 3
print(x)

# maths functions
x = 2.9
print(round(x))
# module
import math
print(math.ceil(2.9))
# if statements in python
is_hot = False
is_cold = True
if is_hot:
    print("Its a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("wear warm clothes")
else:
    print("Its a lovely day")

# problem
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1*price
    print(down_payment)
else:
    down_payment = 0.2*price
print(down_payment)

# logical operators
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for a loan")

# AND: both
# OR: at least one
# not: converts a boolean value
temperature = 30
if temperature > 30:
    print("its a hot day")
else:
    print("its not a hot day")

# problem
name = len(input("What is your name? "))
if name<3:
    print("name must be at least 3 characters")
elif name>50:
    print("name can be a maximum of 50 characaters")
else:
    print("name looks good")


