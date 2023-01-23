
# add
def add(n1, n2):
    return n1 + n2
# subtract
def subtract(n1, n2):
    return n1 - n2
# multiply

def multiply(n1, n2):
    return n1 * n2
# divide
def divide(n1, n2):
    return n1 / n2
operations ={
 "+": add,
 "-": subtract,
 "*": multiply,
 "/": divide
}
def calculator():
    num1 = int(input("what is the first number?: "))
    num2 = int(input("what is the second number?: "))
    for symbols in operations:
        print(symbols)
        should_continue = True
    while should_continue:
        operational_symbol = input("Pick an operation: ")
        num2 = int(input("what is the number?: "))
        calculation_function = operations[operational_symbol]
        answer = calculation_function(num1, num2)
        print(f" {num1} {operational_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_contine = False
calculator()