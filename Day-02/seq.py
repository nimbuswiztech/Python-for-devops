# String examples
name = "Alice"
message = 'Hello, World!'
multiline = """This is a
multiline string"""

print(f"Name: {name}, Type: {type(name)}")

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation
print(f"Full name: {full_name}")

# String methods
text = "  Python Programming  "
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Uppercase: '{text.upper()}'")
print(f"Lowercase: '{text.lower()}'")
print(f"Replace: '{text.replace('Python', 'Java')}'")

# String indexing and slicing
word = "Programming"
print(f"First character: {word[0]}")
print(f"Last character: {word[-1]}")
print(f"Slice [0:4]: {word[0:4]}")
print(f"Length: {len(word)}")

# String formatting
age = 30
formatted = f"I am {age} years old"  # f-string (Python 3.6+)
print(formatted)



print(f"------  list -----")
  
# List examples
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
empty_list = []

print(f"Numbers: {numbers}, Type: {type(numbers)}")

# List operations
fruits = ["apple", "banana", "orange"]
print(f"Original list: {fruits}")

# Adding elements
fruits.append("grape")  # Add to end
fruits.insert(1, "mango")  # Insert at index 1
print(f"After additions: {fruits}")

# Removing elements
fruits.remove("banana")  # Remove by value
popped = fruits.pop()  # Remove and return last element
print(f"After removal: {fruits}")
print(f"Popped element: {popped}")

# List indexing and slicing
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")

# List comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# Other useful methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")
numbers.sort()  # Sort in place
print(f"Sorted: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Count of 5: {numbers.count(5)}")

print(f"------  tuple -----")


# Tuple examples
coordinates = (10, 20)
colors = ("red", "green", "blue")
mixed_tuple = (1, "hello", 3.14, True)
single_element = (42,)  # Note the comma for single element tuple

print(f"Coordinates: {coordinates}, Type: {type(coordinates)}")

# Tuple operations (limited due to immutability)
point = (5, 10, 15)
print(f"Point: {point}")
print(f"X coordinate: {point[0]}")
print(f"Y coordinate: {point[1]}")
print(f"Z coordinate: {point[2]}")

# Tuple unpacking
x, y, z = point
print(f"Unpacked - X: {x}, Y: {y}, Z: {z}")

# Removing elements
point.remove("10")  # Remove by value
popped = point.pop()  # Remove and return last element
print(f"After removal: {point}")
print(f"Popped element: {popped}")

# Tuple methods
numbers_tuple = (1, 2, 3, 2, 4, 2)
print(f"Count of 2: {numbers_tuple.count(2)}")
print(f"Index of 3: {numbers_tuple.index(3)}")
print(f"Length: {len(numbers_tuple)}")

# Converting between list and tuple
list_from_tuple = list(colors)
tuple_from_list = tuple([1, 2, 3])
print(f"List from tuple: {list_from_tuple}")
print(f"Tuple from list: {tuple_from_list}")