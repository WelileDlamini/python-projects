import logo
from data import data
import random
# display art
print(logo)

score = 0

def format_data(account):
   account_name = account["name"]
   account_descr = account["description"]
   account_country = account["country"]
   return(f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    """use if statements to check if user is correct."""
    if a_followers > b_followers:
        if guess == "a"
            return True
        else:
            return False
# generate a random account
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)
print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")
# ask a user for a guess
guess = input("who has more followers? Type 'A' or 'B': ").lower()

# check if user is correct
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]
# give user feedback on their guess
is_correct = check_answer(guess,a_follower_count, b_follower_count)
if is_correct:
    score +=1
    print(f"You are right! current score {score} ")
else:
    print(f"sorry thats wrong final score is {score}")

# make the game repeatable

# making the account B become the next position