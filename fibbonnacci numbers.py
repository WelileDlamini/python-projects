def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(20):
    print(x)

# using a list
def fib(number):
    a = 0
    b = 1
    result =[]
    for i in range(number):
        fib = a + b
        result.append(fib)
    return result
print(fib(10))