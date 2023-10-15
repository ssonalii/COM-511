# Type Checking
var_str = "Hello, World!"
var_int = 42
var_float = 3.14159265
var_bool = True
var_list = [1, 2, 3, 4, 5]
var_dict = {"name": "John", "age": 30}
var_set = {1, 2, 3}
var_tuple = (10, 20, 30)

# abs() - Absolute Value
print(f"Absolute value of -5: {abs(-5)}")

# len() - Length of Sequence
print(f"Length of list: {len(var_list)}")

# min() - Minimum Value
print(f"Minimum value in list: {min(var_list)}")

# round() - Rounding Floating-Point Numbers
print(f"Rounded value of {var_float}: {round(var_float, 2)}")

# isalnum() - Check if a String is Alphanumeric
string_to_check = "abc123"
print(f"Is '{string_to_check}' alphanumeric? {string_to_check.isalnum()}")

# type() - Get the Type of a Variable
variables = [var_str, var_int, var_float, var_bool, var_list, var_dict, var_set, var_tuple]
for var in variables:
    print(f"The type of {var}: {type(var).__name__}")