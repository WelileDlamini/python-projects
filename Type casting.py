# num_char = len(input('What is your name?'))
# new_num_char = str(num_char)
# print('Your name has ' + new_num_char + 'characters.')
#
# a = str(123)
# print(type(a))
#
# print(70 + float('100.5'))
# print(str(70) + str(100))



# we can not concatinate strings and integers thus the will be an error here
# num_char = len(input('What is your name?'))
# new_num_char = str(num_char)
# print('Your name' + new_num_char + 'characters.')

a = str(123)
print(type(a))

# interactive coding exercise
two_digit_number = input('type a two digit number')
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)
