# Dictionary examples
person = {"name": "Alice", "age": 30, "city": "New York"}
empty_dict = {}
mixed_dict = {"string": "hello", "number": 42, "list": [1, 2, 3]}

print(f"Person: {person},r: {type(person)}")

# Dictionary operations
student = {
    "name": "John Doe",
    "age": 20,
    "grades": [85, 92, 78, 96],
    "is_enrolled": True
}

# Accessing values
print(f"Student name: {student['name']}")
print(f"Student major: {student.get('major', 'Not found')}")  # Safer access
print(f"student details : {student}")

# Adding/updating values
student["major"] = "Computer Science"
student["age"] = 21  # Update existing key
print(f"Updated student: {student}")
print(f"Student major: {student.get('major', 'Not found')}")  # Safer access

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