# user is asked to input a number 'n' which must satisfy the  condition
n = int(input("Enter a number, n, where -6 < n < 2: "))
# the loop considers numbers that are separated by 7
for i in range(n, n + 42, 7):
    print(i)