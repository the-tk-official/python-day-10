from art import  logo
# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operator = str(input('Pick an operation from the line above: '))
        num2 = float(input("What's the second number?: "))

        operation = operations[operator]
        answer = operation(num1, num2)

        print(f'{num1} {operator} {num2} = {answer}')

        action = str(input(f'Type "y" to continue calculating with {answer} or type "n" to start a new calculation: '))
        if action == 'y':
            num1 = answer
        elif action == 'n':
            should_continue = False
            calculator()
        else:
            should_continue = False

calculator()
