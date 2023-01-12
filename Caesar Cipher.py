# create a function called 'encrypt' that takes the 'text' and 'shift' as inputs
# import and print the logo art.py when the program starts

alphabet = ['a', 'b', 'c' 'd', 'e', 'f', 'g', 'h', 'i', 'j,' 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'a', 'b', 'c' 'd', 'e', 'f', 'g', 'h', 'i', 'j,' 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
         position = alphabet.index(char)
         new_position = position + shift_amount
         end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here is the {cipher_direction}d result: {end_text}")

# try creating a new function that calls itself if they type 'yes'

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text= input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))

# what if the user enters a shift that is greater than the number of letters in the alphabet

# inside the 'encrypt' fuction, shift each letter of the'text' fowards in alphabet by the 'shift' amount and print the encrypted
# create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs
# check if the user wanted to encrypt or decrypt the massage by changing the direction variable
# then call the correct function based on the 'direction' variable
shift = shift % 25
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
if restart == 'no':
    should_continue = False
    print('Goodbye')



