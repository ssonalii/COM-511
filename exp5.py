def reverse_kth_rows(matrix, k):
    for i in range(k - 1, len(matrix), k):
        matrix[i] = matrix[i][::-1]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Input matrix dimensions
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize an empty matrix
matrix = []

# Input matrix values
print(f"Enter {rows}x{cols} matrix values row by row:")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Input value of k
k = int(input("Enter the value of k: "))

if k <= 0 or k > rows:
    print("Invalid value of k. It should be between 1 and the number of rows.")
else:
    # Reverse every kth row
    reverse_kth_rows(matrix, k)

    # Output the modified matrix
    print("\nMatrix with every", k, "th row reversed:")
    print_matrix(matrix)