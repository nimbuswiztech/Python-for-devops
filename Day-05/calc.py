import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# Reading command line arguments
# sys.argv[0] = script name
# sys.argv[1] = first argument (number1)
# sys.argv[2] = second argument (operation)
# sys.argv[3] = third argument (number2)

num1 = float(sys.argv[1])  # Convert string to float
operation = sys.argv[2]
num2 = float(sys.argv[3])  # Convert string to float

# Execute based on operation
if operation == "add":
    output = add(num1, num2)
    print(f"Result: {output}")
elif operation == "sub":
    output = subtract(num1, num2)
    print(f"Result: {output}")
elif operation == "mul":
    output = multiply(num1, num2)
    print(f"Result: {output}")
else:
    print("Invalid operation! Use: add, sub, or mul")