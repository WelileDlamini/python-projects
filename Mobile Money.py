# Define a function to handle user login
def login(username, password):
    # Check if username and password are correct
    if username == "myusername" and password == "mypassword":
        # If correct, return the options for the user
        return "1. Buy\n2. Send Money\n3. Banking\n4. Savings and Invest"
    else:
        # If incorrect, return an error message
        return "Invalid login credentials"


# Ask the user to enter their username and password
username = input( "Enter your username: " )
password = input( "Enter your password: " )

# Call the login function and display the options or error message
print( login( username, password ) )