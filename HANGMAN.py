word_list = ['ardvark', 'baboon', 'camel']
import random
chosen_word = random.choice(word_list)
guess = input('Guess a letter:').lower()
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
display = []
word_length = len(chosen_word)
for _ in range(len(word_length )):
    display += "_"
print(display)

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)
