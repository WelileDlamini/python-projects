def calculator():
    print( "Welcome to the calculator!" )
    num1 = float( input( "Enter the first number: " ) )
    operator = input( "Enter the operator (+, -, *, /): " )
    num2 = float( input( "Enter the second number: " ) )

    if operator == "+":
        result = num1 + num2
        print( num1, operator, num2, "=", result )
    elif operator == "-":
        result = num1 - num2
        print( num1, operator, num2, "=", result )
    elif operator == "*":
        result = num1 * num2
        print( num1, operator, num2, "=", result )
    elif operator == "/":
        result = num1 / num2
        print( num1, operator, num2, "=", result )
    else:
        print( "Invalid operator. Please try again." )


# call the calculator function
calculator()

# This calculator takes in two numbers and an operator, performs the operation, and outputs the result. If the operator entered is invalid, the program will display an error message.
