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
print(course.replace('Beginners', 'Absolute Beginners')

