def highest_even(li):
    evens = []
    for item in li:
        if item %2 == 0:
          evens.append(item)
    return max(evens)
print(highest_even([10,2,3,4,8,11]))

# Walrus Operator
# assigns values to variables as part of a larger expression
a = ' hellooooooooo'

if ((n := len(a))>10):
    print(f'too long {n} elements')

while ((n:= len(a))> 1):
    print(n)
    a = a[:-1]
print(a)

# scope = what variables do I have acces to
# global

total = 0
def count():
    global total
    total += 1
    return total


print(count())