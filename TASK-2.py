# Simple Calculator Program

def calculator():
    print("Welcome to Simple Calculator")

    # Get input from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Choose operation
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    # Perform operation based on choice
    if choice == '1':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid operation choice.")

# Run the calculator
calculator()
