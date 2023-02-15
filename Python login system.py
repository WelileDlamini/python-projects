# write a code for a python login system
users = {'username1': 'password1', 'username2': 'password2', 'username3': 'password3'}

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")
        login()

login()