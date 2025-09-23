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