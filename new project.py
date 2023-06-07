#
my_list = [1,2,3,4,6,7,8,9,10]
cont = 0
for i in my_list:
    cont += i
print(cont)

# range
for number in range(0,10):
    print("email email list")

for _ in range(10,0,-2):
    print(_)
for _ in range(2):
    print(list(range(10)))

# enumerate
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is: {i}')


