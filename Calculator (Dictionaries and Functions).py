#calculator


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
operations =\
{
 "+": add,
 "-": subtract,
 "*": multiply,
 "/": divide
}
num1 = int(input("what is the first number?: "))
num2 = int(input("what is the second number?: "))

for symbols in operations:
    print(symbols)
operational_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operational_symbol]
answer = calculation_function(num1, num2)


print(f" {num1} {operational_symbol} {num2} = {answer}")



