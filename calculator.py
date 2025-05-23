import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is undefined.")
        return None
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Welcome to the Simple Calculator!")
    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide),
        '5': ('Power', power),
        '6': ('Modulus', modulus),
        '7': ('Exit', None)
    }

    while True:
        print("\nSimple Calculator")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("Select operation (1-7): ")

        if choice not in operations:
            print("Invalid selection. Please choose a valid option.")
            continue

        if choice == '7':  # Exit
            print("Exiting calculator. Goodbye!")
            sys.exit()

        op_name, op_func = operations[choice]
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        result = op_func(num1, num2)
        if result is not None:
            print(f"Result of {op_name.lower()}ing {num1} and {num2} = {result}")

if __name__ == "__main__":
    main()
