# Iterate over a list of numbers and print each number
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# Iterate over a range of numbers and print each number
for i in range(5):  # This will iterate from 0 to 4
    print(i)

# Iterate over each character in a string and print each character
text = "Hello"

for char in text:
    print(char)

# Iterate over the keys and values of a dictionary
student_scores = {'shivani': 85, 'diya': 90, 'riya': 78}

for student, score in student_scores.items():
    print(f"{student}: {score}")

# Iterate over a 2D list (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=' ')
    print()  # For a new line after each row

# Iterate over a list with index and value
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
