import math

while True:
    try:
        # Get first number and operator
        num1 = float(input("What is the first number? "))
        op = input(
            "What operation do you want to perform (e.g., +, -, *, /, **, sqrt(x))? (or q to quit) ")

        # Quit option
        if op.lower() in ("q", "quit"):
            break

        # Handle square root separately (doesn't need second number)
        if op == "sqrt(x)":
            if num1 < 0:
                print("Cannot take the square root of a negative number.")
            else:
                print(math.sqrt(num1))
        else:
            # Get second number for all other operations
            num2 = float(input("What is the second number? "))

            if op == "+":
                print(num1 + num2)
            elif op == "-":
                print(num1 - num2)
            elif op == "*":
                print(num1 * num2)
            elif op == "/":
                print(num1 / num2)
            elif op == "**":
                print(num1 ** num2)
            else:
                print("Please input a valid operation.")
    except ValueError:
        print("Please input a valid number")
    except ZeroDivisionError:
        print("Division by zero not allowed.")
