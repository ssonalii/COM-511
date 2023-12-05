# Function to find the largest of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# Function to check if a number is Armstrong or not
def is_armstrong(number):
    num_str = str(number)
    num_length = len(num_str)
    armstrong_sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** num_length
        temp //= 10
    return number == armstrong_sum

# Taking user inputs for three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding the largest of the three numbers using max_of_three function
largest_number = max_of_three(num1, num2, num3)
print("The largest number is:", largest_number)

# Taking user input to check if a number is an Armstrong number
number_to_check = int(input("\nEnter a number to check if it's Armstrong: "))
if is_armstrong(number_to_check):
    print(f"{number_to_check} is an Armstrong number")
else:
    print(f"{number_to_check} is not an Armstrong number")
