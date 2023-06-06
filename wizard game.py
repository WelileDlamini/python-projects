is_magicain = True
is_expert = False

if is_magicain and is_expert:
    print('you are a master magician')
elif is_magicain == True and is_expert != True:
    print('at least you getting there')
elif is_magicain != True:
    print('you need magic powers')

# loops
for item in 'Zero to Mastery':
    print(item)

# iterables
# collection of items
# go 1 by 1 to check each item in the collection
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim':  False
}
for item in user.items():
    print(item)

# or
for key,value in user.items():
    print(key,value)

for item in user.values():
    print(item)
for item in user.keys():
    print(item)
