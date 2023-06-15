def hello(func):
    func()

def greet():
    print('still here!')

a = hello(greet)
print(a)

# higher order functions
def greet(func): # a function that accepts another function
    func()

def greet2():
    def func(): # function that returns another function
        return 5
    return func

# decorator
def my_decorator(func):
    def wrap_func():
        print('******')
        func()
        print('*******')
    return wrap_func

@my_decorator
def hello():
    print('hell0')


@my_decorator
def bye():
    print('see you later')
hello()
bye()
# or
hello2 = my_decorator(hello)
hello2()
#decorator pattern
def my_decorator(func):
    def wrap_func(*arg, **kwargs):
        print('******')
        func(*arg, **kwargs)
        print('*******')
    return wrap_func

@my_decorator
def hello(greeting, emoji=":("):
    print(greeting, emoji)
hello('hiii')

# decorators
# perfomance decorator

from time import time
def perfomance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'It took {t2-t1}s')
        return result
    return wrapper

@perfomance
def long_time():
    for i in range(10000000):
        i*5

long_time()





