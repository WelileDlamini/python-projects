# using reversed()method
myString = "PythonForBeginners"
reverse_iterator = reversed(myString)
reversedString = ""
for character in reverse_iterator:
    reversedString = reversedString + character
print(f"Original string is: {myString}")
print(f"Reversed string is: {reversedString}")

# using slicing method
myString = "PythonForBeginners"
reversedString = myString[:: -1]
print("Original String is:", myString)
print("Reversed String is:", reversedString)
