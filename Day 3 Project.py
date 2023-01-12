print("Welcome to the treasure Island")
print("Your mission is to find the treasure")
choice1 = input('You re are at crossroad, where do you want to go?, left or  right.').lower()
if choice1 == "left":
    choice2 = input("You came to a lake. There is a an island in the middle of the lake. Type 'wait' to wait for the boat.Type 'swim' to swim accros").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at an island. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?").lower()
        if choice3 == "red":
            print("game is over stay please")
        elif choice3 == "blue":
            print("game over, you are useless")
        elif choice3 == "yellow":
            print("you are a star, you won.")
    else:
        print("game over")
else:
    print("game over, you dont know what you are doing.")

