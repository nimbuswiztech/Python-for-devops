# Integer examples
age = 25
negative_number = -10
large_number = 1000000

# You can use underscores for readability in large numbers
million = 1_000_000

print(f"Age: {age}, shubham  {type(age)}")
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
print(f"Pi: {result}, Type: {type(result)}")
print(f"Is equal to 0.30000000000000004? {result == 0.30000000000000004}")

# Using round() for precision
print(f"Rounded result: {round(result, 1)}")


print(f"--- complex values -----")
# ----- complex data type -----

# Complex number examples
z1 = 3 + 4j
z4 = complex(3, 4)  # Another way to create a complex number
z2 = complex(2, 5)  # 2 + 5j
z3 = 1j  # Pure imaginary number

print(f"Complex number z1: {z1} Type: {type(z1)}")
print(f"Real part: {z1.real}")
print(f"Imaginary part: {z1.imag}")

# Complex operations
result = z1 + z2
print(f"Addition: {z1} + {z2} = {result}")
print(f"Multiplication: {z1} * {z2} = {z1 * z2}")
print(f"Conjugate of z1: {z1.conjugate()}")
print(f"Absolute value: {abs(z1)}")