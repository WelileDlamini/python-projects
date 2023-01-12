print('Welcome to the roller coaster')
height = int(input('What is your height in cm? '))
bill = 0
if height > 120:
    print('You can ride the roller_coaster')
    age = int(input('What is your age'))
    if age < 12:
        bill = 5
        print('Child tickets are $5')
    elif age < 18:
         bill = 7
         print('Youth tickets are $7')
    elif (age > 45) and (age < 55):
        print("Free ride")
    else:
        bill = 12
        print('Adult tickets are $12')
    wants_photo = input('Do you want a photo taken? Y or N. ')
    if wants_photo == 'Y':
        new_bill = bill + 3
        print(f'Your final bill is {new_bill}')
else:
    print('Sorry, you have to grow taller before you can ride.')

# Love calculator
print("Welcome to the Love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name?\n")
combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("t")
u = lower_case_string.count("t")
e = lower_case_string.count("t")

true = int(t + r + u + e)

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = int(l + o + v + e)

total_score = true + love

if (love < 10) or (love > 90):
    print(f"Your score is, {total_score}, you look great together")
elif (love >= 40) and (love <= 50):
    print(f"Your score is, {total_score}, you look fine together")
else:
    print(f"Your final score is, {total_score}")





