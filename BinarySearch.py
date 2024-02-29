# if target is less than mid ignore the right part, 
# else if target is greater ignore the left part

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid

        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1

        # If the target is smaller, ignore the right half
        else:
            right = mid - 1

    # If we reach here, then the element was not present
    return -1

# Example usage
sorted_array = [2, 5, 8, 12, 16, 23, 38, 42, 50]
target_value = int(input('enter number which needs to be searched'))

result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not present in the array")
