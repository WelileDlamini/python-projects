# conditional logic
is_old = True
is_linsence = True
if is_old:
    print('you are old enough')
elif is_linsence:
    print('you can drive now')
else:
    print('you are not of age')
print('okoko')

# indentation in python
# truthy and falsly
is_old = bool('hello')
is_linsence =  bool(5)
if is_old:
    print('you are old enough')
elif is_linsence:
    print('you can drive now')
# truthy value
print(bool('hello'))
print(bool(5))
# falsey value
print(bool(''))
print(bool(0))
###
password = '123'
username = 'jonny'
if password and username:
    print('you are old enough')
else:
    print('you are not of ')