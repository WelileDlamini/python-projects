# generate a number 1, 10
# input from user
# check that the input is a number 1,10
# check if the number is the right guess. Otherwise
# ask again

from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))


while True:
    number = int( input( 'guess a number  between 1 and 10:  ' ) )
    try:
        if number < 1 and number > 10:
            if number == answer:
                print("you are a star")
                print("All good congradulations")
                break
        else:
            print('Please values between 1 to 10')

    except ValueError:
        print('please enter a number')
        continue




