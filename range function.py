total = 0
for numbers in range(1, 101):
    total += numbers
print(total)

total = 0
for numbers in range(1, 101):
    if numbers % 2 == 0:
        total += numbers
print(total)