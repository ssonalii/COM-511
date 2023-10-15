def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1  # Element not found


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Element not found


# Input list (sorted for binary search)
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Target element to search for
target = 11

# Perform Linear Search
linear_result = linear_search(sorted_list, target)
if linear_result != -1:
    print(f"Linear Search: Element {target} found at index {linear_result}")
else:
    print("Linear Search: Element not found")

# Perform Binary Search
binary_result = binary_search(sorted_list, target)
if binary_result != -1:
    print(f"Binary Search: Element {target} found at index {binary_result}")
else:
    print("Binary Search: Element not found")