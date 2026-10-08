# Simple Calculator


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def modulus(a, b):
    return a % b


while True:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nSelect Operation:")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")
    print("% Modulus")

    operation = input("Enter operation: ")

    if operation == "+":
        result = addition(num1, num2)

    elif operation == "-":
        result = subtraction(num1, num2)

    elif operation == "*":
        result = multiplication(num1, num2)

    elif operation == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            continue
        result = division(num1, num2)

    elif operation == "%":
        if num2 == 0:
            print("Cannot divide by zero.")
            continue
        result = modulus(num1, num2)

    else:
        print("Invalid operation.")
        continue

    print("Result:", result)

    again = input("\nDo you want to perform another calculation? (yes/no): ")

    if again.lower() != "yes":
        print("Calculator closed.")
        break