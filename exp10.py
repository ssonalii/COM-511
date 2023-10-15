# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator function
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide,
    }

    if choice in operations:
        result = operations[choice](num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid input. Please select a valid operation.")

while True:
    calculator()
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        print("Goodbye!")
        break
