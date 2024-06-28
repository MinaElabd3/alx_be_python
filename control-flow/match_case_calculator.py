def match_case_calculator():
    # Prompt for user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose the operation (+, -, *, /): ")

    # Perform calculation based on operator using match case
    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            result = num1 / num2
        case _:
            print(f"Invalid operator '{operator}'. Please choose from '+', '-', '*', '/'.")

    # Output the result
    if operator in ['+', '-', '*']:
        print(f"The result of {num1} {operator} {num2} is {result}.")
    elif operator == '/':
        if num2 != 0:
            print(f"The result of {num1} {operator} {num2} is {result}.")
    else:
        print("Operation not performed due to invalid operator.")

# Run the calculator function
match_case_calculator()

