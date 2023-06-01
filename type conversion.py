name = 'Welile Dlamini'
age = 50
relationship_status = 'single'
relationship_status = 'it\'s complicated'
print(relationship_status)

# guessing year
birth_year = int(input('what year were you born?'))
current_year = int(input('what is the current year?'))
age = current_year - birth_year
s = f'Your age is {age} thank you'
print(s)

# password checker
user_name = input('Whats your user name?')
password = input ('Whats your password')
length = len(password)
encryption = '*'*length
s = f'{user_name}, your password {encryption}, is {length} letters long'
print(s)

# list slicing
amazon_cart = ['notebooks', 'sunglasses','welile', 'dlamini']
print(amazon_cart[0::2])
amazon_cart[0]= 'laptop'
print(amazon_cart)

# matrix 2D list
matrix = [[1,2,3],[2,4,6],[7,8,9]]
print(matrix[0][1])
