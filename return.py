def sum(num1,num2):
    def another_function(n1,n2):
        return n1 + n2
    return another_function(num1,num2)

total = sum(10,20)
print(total)

# methods vs Functions
# doc string
# clean code
def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    return False
print(is_odd_or_even(51))

# arguments and key word arguments
# *arg **kwargs

def super_func(*arg, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(arg) + total
print(super_func(1,2,3,4,5, num1= 5, num2= 10))

# rule: params, *arg, default parameters, **kwargs

