def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

while True:
    print("\nTemperature Conversion")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        except ValueError:
            print("Invalid input. Please enter a valid temperature.\n")
    elif choice == "2":
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        except ValueError:
            print("Invalid input. Please enter a valid temperature.\n")
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1, 2, or 3).\n")