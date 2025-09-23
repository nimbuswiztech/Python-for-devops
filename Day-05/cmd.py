import sys

def add(a, b):
    return a + b

def sub(a, b):
    return a - b   

def mul(a, b):
    return a ** b   

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a // b


num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])


#command line arguments
#sys.argv[0] # script name
#sys.argv[1] # first argument
#sys.argv[2] # second argument
#sys.argv[3] # third argument


if operation == "add":
    result = add(num1, num2)
    print(f"The result of adding {num1} and {num2} is: {result}")
elif operation == "sub":
    result = sub(num1, num2)
    print(f"The result of subtracting {num2} from {num1} is: {result}")
elif operation == "mul":
    result = mul(num1, num2)
    print(f"The result of multiplying {num1} and {num2} is: {result}")
elif operation == "div":
    result = div(num1, num2)
    print(f"The result of dividing {num1} by {num2} is: {result}")
else:
    print("Error: Invalid operation. Please use 'add', 'sub', 'mul', or 'div'.")

