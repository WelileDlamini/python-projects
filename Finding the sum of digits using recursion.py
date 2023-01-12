def sum_of_digits(n):
    assert n>=0 and int(n) == n, 'The number has a positive integer only'
    if n == 0:
        return 0
    else:
        return int(n%10) + sum_of_digits(int(n/10))
print(sum_of_digits(3456))


# calculating powers using recursion
def power(base, exp):
    assert int(exp) == exp, 'The exponent must be integer number only'
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * power(base, exp+1)
    return base * power(base, exp-1)


# calculating GCD using recursion
def gcd(a,b):
    assert int(a) == a and int(b) == b,'The number integer only'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(48,1.8))

# decimal to binary using recursion
def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be an integer only'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinary(int(n/2))
print(decimalToBinary(13))





