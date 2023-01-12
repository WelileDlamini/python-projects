def factorial(n):
    assert n >=0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(10))


# calculating Fibonacci numbers using Recursion
def fibonacci(n):
    assert n >= 0 and int(n) == n,'Fibonacci number can not be nagative number or non integer'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(2))
