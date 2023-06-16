def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result
my_list = make_list(100)
print(my_list)

print(list(range(100000)))

# generator
def generator_function():
    for i in range(10):
        yield i


for item in generator_function(100):
    print(item)

g = generator_function(100)
next(g)
next(g)
print(next(g))

# generator perfomance
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
    print('1')
    for i in range(100):
        i*5

@perfomance
def long_time2():
    for i in range(10000000):
        i*5

long_time()
long_time2()