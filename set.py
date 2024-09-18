# Creating an empty set
empty_set = set()

# Creating a set with elements
numbers = {1, 2, 3, 4, 5}

# Creating a set from a list (duplicates are removed)
fruits = set(["apple", "banana", "apple", "orange"])  # {'apple', 'banana', 'orange'}


# Iterating over a set
for fruit in fruits:
    print(fruit)


# Adding an element
numbers.add(6)

# Removing an element (raises KeyError if element not present)
numbers.remove(3)

# Removing an element if present (does not raise error if element is not present)
numbers.discard(7)

# Popping an arbitrary element (removes and returns it)
popped_element = numbers.pop()


# Union of sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b  # {1, 2, 3, 4, 5}

# Intersection of sets
intersection_set = set_a & set_b  # {3}

# Difference of sets
difference_set = set_a - set_b  # {1, 2}

# Symmetric Difference (elements in either set, but not in both)
sym_diff_set = set_a ^ set_b  # {1, 2, 4, 5}


# Checking if a set is a subset of another
is_subset = {1, 2}.issubset(set_a)  # True

# Checking if a set is a superset of another
is_superset = set_a.issuperset({2, 3})  # True

# Checking for disjoint sets (no common elements)
is_disjoint = set_a.isdisjoint({6, 7})  # True


# Basic set comprehension
squares = {x**2 for x in range(6)}  # {0, 1, 4, 9, 16, 25}

# Conditional set comprehension
even_squares = {x**2 for x in range(6) if x % 2 == 0}  # {0, 4, 16}

# Length of a set
length = len(set_a)  # Number of elements in set_a

# Checking for membership
is_in_set = 3 in set_a  # True


# Shallow copy of a set
copied_set = set_a.copy()

# Note: Sets are mutable, so a shallow copy is usually sufficient.


# Creating a frozenset
immutable_set = frozenset([1, 2, 3, 4])

# Operations with frozensets (most are similar to regular sets)
# Note: frozensets do not support methods that modify the set


# Removing duplicates from a list
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(original_list)  # {1, 2, 3, 4, 5}

# Set operations in data analysis
group_a = {1, 2, 3, 4, 5}
group_b = {4, 5, 6, 7, 8}
print("Common members:", group_a & group_b)  # {4, 5}
print("Exclusive to group_a:", group_a - group_b)  # {1, 2, 3}
print("All members:", group_a | group_b)  # {1, 2, 3, 4, 5, 6, 7, 8}

