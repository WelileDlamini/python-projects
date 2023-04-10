message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😂",
    ":(": "😥"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

# funtions
def greet_user():
    print("Hi there")
    print("Welcome aboard")


print("start")
greet_user()
print("finish")

# parameter
def greet_user(name, last_name):
    print(f'Hi, {name} {last_name }!')
    print('Welcome onboard')
greet_user("John", "Dlamini")
greet_user("Mary")
