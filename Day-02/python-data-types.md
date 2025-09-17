# Python Data Types - Complete Guide with Examples

## Overview
Data types in Python determine how data is stored in memory and what operations can be performed on that data. Python is dynamically typed, meaning you don't need to explicitly declare variable types.

## 1. Numeric Data Types

### Integer (int)
Represents whole numbers without decimal points.

```python
# Integer examples
age = 25
negative_number = -10
large_number = 1000000

# You can use underscores for readability in large numbers
million = 1_000_000

print(f"Age: {age}, Type: {type(age)}")
print(f"Large number: {million}")

# Integer operations
a = 10
b = 3
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")  # Returns float
print(f"Floor Division: {a // b}")  # Returns integer
print(f"Modulus: {a % b}")
print(f"Power: {a ** b}")
```

### Float
Represents numbers with decimal points.

```python
# Float examples
pi = 3.14159
temperature = -5.5
scientific_notation = 1.5e4  # 15000.0

print(f"Pi: {pi}, Type: {type(pi)}")
print(f"Scientific notation: {scientific_notation}")

# Float operations
x = 10.5
y = 2.3
print(f"Float addition: {x + y}")
print(f"Float division: {x / y}")

# Precision considerations
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")  # May not be exactly 0.3
print(f"Is equal to 0.3? {result == 0.3}")

# Using round() for precision
print(f"Rounded result: {round(result, 1)}")
```

### Complex
Represents complex numbers with real and imaginary parts.

```python
# Complex number examples
z1 = 3 + 4j
z2 = complex(2, 5)  # 2 + 5j
z3 = 1j  # Pure imaginary number

print(f"Complex number z1: {z1}")
print(f"Real part: {z1.real}")
print(f"Imaginary part: {z1.imag}")

# Complex operations
result = z1 + z2
print(f"Addition: {z1} + {z2} = {result}")
print(f"Multiplication: {z1} * {z2} = {z1 * z2}")
print(f"Conjugate of z1: {z1.conjugate()}")
print(f"Absolute value: {abs(z1)}")
```

## 2. Sequence Types

### String (str)
Represents sequences of characters.

```python
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
```

### List
Represents ordered, mutable sequences.

```python
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
print(f"Count of 1: {numbers.count(1)}")
```

### Tuple
Represents ordered, immutable sequences.

```python
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
```

## 3. Mapping Type

### Dictionary (dict)
Represents key-value pairs.

```python
# Dictionary examples
person = {"name": "Alice", "age": 30, "city": "New York"}
empty_dict = {}
mixed_dict = {"string": "hello", "number": 42, "list": [1, 2, 3]}

print(f"Person: {person}, Type: {type(person)}")

# Dictionary operations
student = {
    "name": "John Doe",
    "age": 20,
    "grades": [85, 92, 78, 96],
    "is_enrolled": True
}

# Accessing values
print(f"Student name: {student['name']}")
print(f"Student age: {student.get('age', 'Not found')}")  # Safer access

# Adding/updating values
student["major"] = "Computer Science"
student["age"] = 21  # Update existing key
print(f"Updated student: {student}")

# Dictionary methods
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Iterating through dictionary
print("\nIterating through dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dictionary: {squares_dict}")

# Nested dictionaries
company = {
    "employees": {
        "john": {"age": 30, "department": "IT"},
        "jane": {"age": 25, "department": "HR"}
    }
}
print(f"John's department: {company['employees']['john']['department']}")
```

## 4. Set Types

### Set
Represents unordered collections of unique elements.

```python
# Set examples
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14}
empty_set = set()  # Note: {} creates an empty dict, not set

print(f"Numbers set: {numbers}, Type: {type(numbers)}")

# Set operations
fruits = {"apple", "banana", "orange"}
print(f"Original fruits: {fruits}")

# Adding elements
fruits.add("grape")
fruits.update(["mango", "kiwi"])  # Add multiple elements
print(f"After additions: {fruits}")

# Removing elements
fruits.remove("banana")  # Raises error if not found
fruits.discard("pineapple")  # Doesn't raise error if not found
print(f"After removal: {fruits}")

# Set operations (mathematical)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")  # or set1.union(set2)
print(f"Intersection: {set1 & set2}")  # or set1.intersection(set2)
print(f"Difference: {set1 - set2}")  # or set1.difference(set2)
print(f"Symmetric difference: {set1 ^ set2}")

# Practical use case: removing duplicates
duplicate_list = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = list(set(duplicate_list))
print(f"Original with duplicates: {duplicate_list}")
print(f"Unique numbers: {unique_numbers}")
```

### Frozenset
Represents immutable sets.

```python
# Frozenset examples
immutable_set = frozenset([1, 2, 3, 4, 5])
empty_frozenset = frozenset()

print(f"Frozenset: {immutable_set}, Type: {type(immutable_set)}")

# Frozenset operations (similar to set but immutable)
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

print(f"Frozenset 1: {fs1}")
print(f"Frozenset 2: {fs2}")
print(f"Union: {fs1 | fs2}")
print(f"Intersection: {fs1 & fs2}")

# Use case: as dictionary keys (sets can't be keys, but frozensets can)
set_dict = {
    frozenset([1, 2]): "first pair",
    frozenset([3, 4]): "second pair"
}
print(f"Dictionary with frozenset keys: {set_dict}")
```

## 5. Boolean Type

### Bool
Represents True or False values.

```python
# Boolean examples
is_valid = True
is_complete = False

print(f"Is valid: {is_valid}, Type: {type(is_valid)}")

# Boolean operations
a = True
b = False

print(f"AND: {a and b}")
print(f"OR: {a or b}")
print(f"NOT a: {not a}")
print(f"NOT b: {not b}")

# Truthiness in Python
print("\nTruthiness examples:")
print(f"bool(1): {bool(1)}")        # True
print(f"bool(0): {bool(0)}")        # False
print(f"bool(''): {bool('')}")      # False (empty string)
print(f"bool('hello'): {bool('hello')}")  # True
print(f"bool([]): {bool([])}")      # False (empty list)
print(f"bool([1, 2]): {bool([1, 2])}")  # True
print(f"bool(None): {bool(None)}")  # False

# Comparison operations return booleans
x = 10
y = 20
print(f"\nComparison operations:")
print(f"{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")

# Boolean in conditional statements
age = 18
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
```

## 6. Binary Types

### Bytes
Represents immutable sequences of bytes.

```python
# Bytes examples
text_bytes = b'Hello, World!'
encoded_bytes = "Hello".encode('utf-8')
byte_array = bytes([72, 101, 108, 108, 111])  # ASCII values for "Hello"

print(f"Text bytes: {text_bytes}, Type: {type(text_bytes)}")
print(f"Encoded bytes: {encoded_bytes}")
print(f"From ASCII values: {byte_array}")

# Bytes operations
data = b'Python Programming'
print(f"Original: {data}")
print(f"First byte: {data[0]}")  # Returns integer (ASCII value)
print(f"Slice [0:6]: {data[0:6]}")
print(f"Length: {len(data)}")

# Converting between string and bytes
original_string = "Hello, 世界"  # Contains Unicode
encoded = original_string.encode('utf-8')
decoded = encoded.decode('utf-8')

print(f"Original string: {original_string}")
print(f"Encoded bytes: {encoded}")
print(f"Decoded back: {decoded}")

# Bytes methods
sample_bytes = b'hello world'
print(f"Uppercase: {sample_bytes.upper()}")
print(f"Replace: {sample_bytes.replace(b'world', b'Python')}")
print(f"Split: {sample_bytes.split()}")
```

### Bytearray
Represents mutable sequences of bytes.

```python
# Bytearray examples
mutable_bytes = bytearray(b'Hello')
empty_bytearray = bytearray()
from_list = bytearray([65, 66, 67, 68])  # ASCII for "ABCD"

print(f"Mutable bytes: {mutable_bytes}, Type: {type(mutable_bytes)}")
print(f"From list: {from_list}")

# Bytearray operations (mutable)
data = bytearray(b'Python')
print(f"Original: {data}")

# Modifying bytearray
data[0] = 74  # ASCII for 'J'
print(f"After modification: {data}")

# Adding to bytearray
data.append(33)  # ASCII for '!'
data.extend(b' Programming')
print(f"After additions: {data}")

# Converting to bytes
immutable_version = bytes(data)
print(f"Converted to bytes: {immutable_version}")

# Practical example: building binary data
binary_data = bytearray()
binary_data.extend([0xFF, 0x00, 0xFF, 0x00])  # Some binary pattern
print(f"Binary data: {binary_data}")
print(f"As hex: {binary_data.hex()}")
```

## 7. None Type

### NoneType
Represents the absence of a value.

```python
# None examples
empty_value = None
result = None

print(f"Empty value: {empty_value}, Type: {type(empty_value)}")

# Common uses of None
def greet(name=None):
    if name is None:
        return "Hello, stranger!"
    return f"Hello, {name}!"

print(greet())
print(greet("Alice"))

# None in data structures
optional_data = [1, 2, None, 4, 5]
print(f"List with None: {optional_data}")

# Dictionary with None values
user_profile = {
    "name": "John",
    "age": 30,
    "email": None,  # Not provided
    "phone": "123-456-7890"
}

# Checking for None
if user_profile["email"] is None:
    print("Email not provided")

# None vs False vs 0 vs empty string
print(f"None is None: {None is None}")
print(f"None == None: {None == None}")
print(f"None == False: {None == False}")
print(f"None == 0: {None == 0}")
print(f"None == '': {None == ''}")

# Function that returns None implicitly
def no_return():
    print("This function doesn't return anything explicitly")

result = no_return()
print(f"Function result: {result}")
```

## 8. Custom Data Types

### Classes and Objects
Create your own data types using classes.

```python
# Custom data type example: Person class
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! {self.name} is now {self.age}")

# Creating instances (objects) of the custom type
person1 = Person("Alice", 25, "alice@email.com")
person2 = Person("Bob", 30, "bob@email.com")

print(f"Person 1: {person1}, Type: {type(person1)}")
print(person1.introduce())
print(f"Name: {person1.name}, Age: {person1.age}")

person1.celebrate_birthday()

# Another custom type: BankAccount
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        return f"Account balance: ${self.balance}"

# Using the custom BankAccount type
account = BankAccount("John Doe", 1000)
print(f"Account type: {type(account)}")
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(f"Transaction history: {account.transaction_history}")
```

## Type Checking and Conversion

```python
# Checking types
value = 42
print(f"Type of {value}: {type(value)}")
print(f"Is integer? {isinstance(value, int)}")
print(f"Is number? {isinstance(value, (int, float))}")

# Type conversion
string_number = "123"
integer_value = int(string_number)
float_value = float(string_number)
print(f"String to int: {integer_value}")
print(f"String to float: {float_value}")

# Converting between types
numbers = [1, 2, 3, 4, 5]
print(f"List to tuple: {tuple(numbers)}")
print(f"List to set: {set(numbers)}")
print(f"Numbers to string: {str(numbers)}")

# Safe conversion with error handling
def safe_int_convert(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

print(f"Safe convert '123': {safe_int_convert('123')}")
print(f"Safe convert 'abc': {safe_int_convert('abc')}")
```

## Summary

Python's built-in data types provide powerful tools for handling different kinds of data:

- **Numeric types** (int, float, complex) for mathematical operations
- **Sequence types** (str, list, tuple) for ordered data
- **Mapping type** (dict) for key-value relationships
- **Set types** (set, frozenset) for unique collections
- **Boolean type** (bool) for logical operations
- **Binary types** (bytes, bytearray) for binary data
- **None type** for representing absence of value
- **Custom types** through classes for specific use cases

Understanding these data types and their characteristics (mutable vs immutable, ordered vs unordered) is crucial for effective Python programming.