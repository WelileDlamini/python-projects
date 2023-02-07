# make a function to set difficulty
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# function to check users guess against actual answer
def check_answer(guess,answer, turns):
    """ Check the answer against guess. Returns the number of turns remmaining"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")
#make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"the correct answer is {answer}")


    turns = set_difficulty()
    #repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print( f"You have {turns} attempts remaining to guess the number:" )
        guess = int(input("make a guess"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You have ran out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again")
# function to check users guess against actual answer
#track the number of turns and reduce by 1 if they get it wrong
#repeat the guessing functionality if they get it wrong.
game()
