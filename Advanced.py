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
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print( "car started" )
    elif command == "stop":
        if not started:
         print("car is already  stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print(""" start- to start the car
         stop- to stop the car
         quit - to quit""")
    elif command == "quit":
        break
    else:
        print("I dont understand")

# for loops
for item in "Python":
    print(item )

# range
for item in range(5,10,2):
    print(item)

# problem
price = [10, 20, 30]
count = 0
for item in price:
    count += item
print(count)

# nested loops
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

# challenge

number = [5, 2, 5, 2, 2]
for x in number:
    output = ""
    for y in range(x):
        output += "x"
        print(output)

# lists

