# error exceptions
# error handling
# syntax error
# name error
# index error
# key error
while True:

    try:
        age = int(input('What is your age'))
        print(age)
    except (ValueError, NameError):
        print('please enter a number')

    except ZeroDivisionError:
        print('please enter a number greater than zero')
    else: # however if the is no error do this
        print('thank you')
        break
# error handling 2
def sum(num1,num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Please enter numbers {err}')
print(sum('1',2))
