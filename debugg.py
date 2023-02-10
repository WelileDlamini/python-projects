# describe problem
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

# reproduce the bug
from random import randint
dice_imgs = ["1","2","3","4","5","6"]
dice_num = randint(0,5)
print(dice_imgs[dice_num])

# play computer
year = int(input("Whats your year of birth?"))
if year > 1980 and year < 1944:
     print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")


