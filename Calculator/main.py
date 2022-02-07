import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

def calculator():
    # Print logo
    print(art.logo)

    # Get first operand.
    num1 = float(input("What's the first number?: "))

    continue_calculation = True
    while continue_calculation:

        # Print out each operator symbols and get operator.
        for symbol in operations:
            print(symbol)
        operator_symbol = input("Pick an operation: ")
        operation = operations[operator_symbol]

        # Get second operand.
        num2 = float(input("What's the next number?: "))

        # Compute and print result.
        answer = operation(num1, num2)
        print(f"{num1} {operator_symbol} {num2} = {answer}")

        res = input(f"Type 'y' to continue calculations with {answer}, or type 'n' to start a new calculation, or type 'x' to exit.: ")
        if res == 'y':
            num1 = answer
        elif res == 'n':
            continue_calculation = False
            calculator()  # Recursive call.
        else:
            continue_calculation = False

calculator()