# Task 2: Simple Calculator - CodSoft

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b


def show_menu():
    print("\n" + "=" * 35)
    print("        SIMPLE CALCULATOR")
    print("=" * 35)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def get_numbers():
    while True:
        try:
            a = float(input("Enter first number : "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input! Please enter numbers only.\n")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please choose between 1 and 5.")
            continue

        a, b = get_numbers()

        if choice == "1":
            result = add(a, b)
            op = "+"
        elif choice == "2":
            result = subtract(a, b)
            op = "-"
        elif choice == "3":
            result = multiply(a, b)
            op = "*"
        elif choice == "4":
            result = divide(a, b)
            op = "/"

        print(f"\nResult: {a} {op} {b} = {result}")


if __name__ == "__main__":
    main()
