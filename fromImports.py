import math
import os
# print(math.sqrt(9))
# from math import sqrt, pi
# # now use the function directly
# print(sqrt(9))

# print(pi)

# it gives you all the fuction that the package contains,
print(dir(math))

print(dir(os))

from BinarySearch import binary_search

sorted_array = [2, 5, 8, 12, 16, 23, 38, 42, 50]
target_value = int(input('enter number which needs to be searched'))

result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not present in the array")
