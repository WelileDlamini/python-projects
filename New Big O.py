# This code finds the sum of the first n integers

def sum_of_n(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

# The time complexity of this code is O(n)