weight = input("What is your weight?: ")
unit = input("(L)bs or (K)g :")
if unit.upper() == "L":
    converted = weight*0.45
    print(f"You are {converted} kilos")
else:
    converted = weight/ 0.45
    print(f"You are {converted} bs")


# while loop
i = 1
while i<= 5:
    print( "*" * i)
    i = i+1
print("Done")

# guessing game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won")
        break
else:
    print("Sorry you failed")

# car game
command = ""
while True:
    command = input(">").lower()
    if command == "start":
        print("car started")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print(""" start- to start the car
         stop- to stop the car
         quit - to quit""")
    elif command == "quit":
        break
    else:
        print("I dont understand")
