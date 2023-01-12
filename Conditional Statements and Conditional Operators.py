# conditional statements
# water_level = 50
# if water_level > 80:
#      print('Drain water')
# else:
#      print('continue')
#
#
#
# # tickets
# print('Welcome to the roller_coaster!')
# height = int(input('What is your height in cm? '))
# if height > 120:
#      print('can ride the roller_coaster')
# else:
#      print('sorry grow taller')
#
# # codding challenge
# number = int(input("What number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#      print("This is an odd number.")


# Nested if statements and elif statements


# interactive coding challenge
# BMI 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)
new_bmi = int(bmi)
if new_bmi > 35:
    if new_bmi > 18.5:
        print(f"Your BMI is {new_bmi}, you are overweight.")
    elif 18.5 < new_bmi < 25:
        print(f"Your BMI is {new_bmi}, you have a normal weight.")
    elif 25 < new_bmi < 30:
        print(f"Your BMI is {new_bmi}, you are slightly overweight.")
    elif 30 < new_bmi < 35:
        print(f"Your BMI is {new_bmi}, you are obese.")
else:
    print(f"Your BMI is {new_bmi}, you are clinically obese.")


# 2 BMI
height = float(input('enter your height in m:'))
weight = float(input('enter your weight in kg:'))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are under weight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese. ")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")