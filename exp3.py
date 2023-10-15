# Input string
input_string = "Welcome to Python world"

# 1. Count the number of alphabets in the string
alphabet_count = sum(1 for char in input_string if char.isalpha())
print(f"1. Number of alphabets in the string: {alphabet_count}")

# 2. Extract characters from a given range (e.g., index 2 to 8)
start_index = 2
end_index = 8
substring = input_string[start_index:end_index]
print(f"2. Substring from index {start_index} to {end_index}: '{substring}'")

# 3. Check if the string is alphanumeric
is_alphanumeric = input_string.replace(" ", "").isalnum()
if is_alphanumeric:
    print("3. The string is alphanumeric.")
else:
    print("3. The string is not alphanumeric.")