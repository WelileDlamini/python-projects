import time

# Function to find the sum of the first n natural numbers
def sum_n(n):
    return (n * (n+1)) // 2

# Function to find the sum of a list of numbers
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Test the sum_n function for different values of n
start = time.time()
print(sum_n(1000))
end = time.time()
print("Time taken:", end-start)

start = time.time()
print(sum_n(1000000))
end = time.time()
print("Time taken:", end-start)

# Test the sum_list function for different lengths of the list
start = time.time()
print(sum_list([1, 2, 3, 4, 5]))
end = time.time()
print("Time taken:", end-start)

start = time.time()
print(sum_list([i for i in range(1000000)]))
end = time.time()
print("Time taken:", end-start)