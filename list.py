# Creating an empty list
empty_list = []

# Creating a list with integers
numbers = [1, 2, 3, 4, 5]

# Creating a list with mixed data types
mixed_list = [1, "apple", 3.14, True]

# Accessing elements by index
first_element = numbers[0]  # 1
last_element = numbers[-1]  # 5

# Slicing lists
sublist = numbers[1:4]  # [2, 3, 4]

# Changing an element
numbers[2] = 10

# Adding elements
numbers.append(6)  # Add to the end
numbers.insert(1, 20)  # Insert at a specific position

# Removing elements
numbers.remove(10)  # Remove first occurrence of value
del numbers[0]  # Remove by index
popped_element = numbers.pop()  # Remove and return last item

# List concatenation
combined_list = numbers + [7, 8, 9]

# List repetition
repeated_list = numbers * 2

# Checking membership
is_in_list = 3 in numbers  # True or False

# Basic list comprehension
squares = [x**2 for x in range(10)]

# Conditional list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Sorting a list (in-place)
numbers.sort()  # Sorts the list in ascending order

# Sorting with a custom key
sorted_list = sorted(numbers, key=lambda x: -x)  # Sorts in descending order

# Reversing a list
numbers.reverse()  # Reverses the list in-place

# Getting the length of a list
length = len(numbers)

# Finding the maximum and minimum values
max_value = max(numbers)
min_value = min(numbers)

# Summing the elements
total_sum = sum(numbers)

# Creating a nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
element = matrix[1][2]  # 6

# Using list comprehension to flatten a nested list
flattened = [item for sublist in matrix for item in sublist]

# Shallow copy
copied_list = numbers.copy()

# Deep copy
import copy
deep_copied_list = copy.deepcopy(numbers)
