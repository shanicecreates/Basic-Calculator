def simp_calculator():
    print("Simp Python Calculator - Enter 'add', 'subtract', 'multiply', 'divide' or 'exit'")

    while True:
        operation = input("Enter operation: ").lower()
        if operation == 'exit':
            break

        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation.")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if operation == 'add':
            print("Result:", a + b)
        elif operation == 'subtract':
            print("Result:", a - b)
        elif operation == 'multiply':
            print("Result:", a * b)
        elif operation == 'divide':
            print("Result:", a / b if b != 0 else "Error: Division by zero")

