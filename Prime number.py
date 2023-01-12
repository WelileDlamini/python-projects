# prime number checker
def prime_checker(number):
    if number % 1 == 0:
        print('This is a prime number')
        if number % number == number:
            print('This is a prime number')
    else:
        print('This is not a prime number')
n = int(input("Check this number: "))
prime_checker(number=n)