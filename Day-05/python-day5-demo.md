# Python for DevOps - Day 5: Command Line Arguments & Environment Variables Demo

## Overview
This demo covers Day 5 of the Python for DevOps series, focusing on command line arguments and environment variables - essential concepts for DevOps engineers.

## What We Learnt (Recap)
- Functions in Python
- Modules and packages
- Installing modules from PyPI using pip
- Virtual environments
- Calculator function example with hardcoded values

## Today's Learning Objectives
1. **Command Line Arguments** - How to pass inputs to Python programs
2. **Environment Variables** - How to handle sensitive information securely

---

## Problem with Hardcoded Values

### Original Calculator (Day 4)
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# Hardcoded values - not flexible!
result_add = add(5, 10)
result_sub = subtract(10, 5)
result_mul = multiply(10, 5)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")
print(f"Multiplication: {result_mul}")
```

**Issues:**
- Always produces the same output
- Users must modify source code to change values
- Not practical for real-world applications

---

## Command Line Arguments

### Why Command Line Arguments?
Real applications like calculators or AWS CLI accept user inputs without modifying source code:
- `python calculator.py 2 add 3`
- `aws s3 ls` (s3 and ls are command line arguments)

### Using the `sys` Module
The `sys` module is built into Python installation - no pip install needed!

### Updated Calculator with Command Line Arguments

```python
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
```

### How to Execute
```bash
python calculator_new.py 2 add 3
# Output: Result: 5.0

python calculator_new.py 10 sub 5
# Output: Result: 5.0

python calculator_new.py 4 mul 6
# Output: Result: 24.0
```

### Important Notes
1. **String to Number Conversion**: Arguments are read as strings by default
   - Use `int()` for integers
   - Use `float()` for decimal numbers (recommended for calculators)
2. **Index Positions**: 
   - `sys.argv[0]` = script name
   - `sys.argv[1]` = first user argument
   - `sys.argv[2]` = second user argument, etc.

---

## Environment Variables

### Why Environment Variables?
For **sensitive information** that shouldn't be visible in:
- Command line history
- CI/CD pipeline files
- Source code

Examples of sensitive data:
- Passwords
- API keys
- Tokens
- Certificates

### Setting Environment Variables

#### Method 1: Terminal Export
```bash
export PASSWORD=mypassword123
export API_TOKEN=abc123xyz789
```

#### Method 2: View Current Environment Variables
```bash
env
```

### Reading Environment Variables in Python

```python
import os

# Reading environment variables
password = os.getenv('PASSWORD')
api_token = os.getenv('API_TOKEN')

print(f"Password: {password}")
print(f"API Token: {api_token}")
```

### Complete Example with Environment Variables

```python
import os

def connect_to_database():
    # Reading sensitive information from environment variables
    db_password = os.getenv('DB_PASSWORD')
    api_key = os.getenv('API_KEY')
    
    if db_password and api_key:
        print("Connecting to database...")
        print(f"Using API Key: {api_key[:10]}...")  # Show only first 10 chars
        return True
    else:
        print("Missing required environment variables!")
        return False

# Usage
if connect_to_database():
    print("Connection successful!")
else:
    print("Connection failed!")
```

### Setting up the Example
```bash
export DB_PASSWORD=supersecret123
export API_KEY=your_api_key_here
python database_example.py
```

---

## Command Line Args vs Environment Variables

| Aspect | Command Line Arguments | Environment Variables |
|--------|----------------------|---------------------|
| **Use Case** | User inputs, configuration options | Sensitive information |
| **Visibility** | Visible in command history | Hidden from casual view |
| **Security** | Less secure for sensitive data | More secure |
| **CI/CD Usage** | Exposed in pipeline files | Can be set securely in runners |
| **Python Module** | `sys` | `os` |
| **Reading Method** | `sys.argv[index]` | `os.getenv('VAR_NAME')` |

---

## Practical DevOps Examples

### 1. AWS CLI Style Tool
```python
import sys
import os

def list_s3_buckets():
    aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region = sys.argv[1] if len(sys.argv) > 1 else 'us-east-1'
    
    print(f"Listing S3 buckets in region: {region}")
    # AWS SDK code would go here

# Usage: python aws_tool.py us-west-2
```

### 2. CI/CD Pipeline Script
```python
import sys
import os

def deploy_application():
    environment = sys.argv[1]  # dev, staging, prod
    deployment_key = os.getenv('DEPLOYMENT_KEY')
    
    if not deployment_key:
        print("Error: DEPLOYMENT_KEY environment variable not set")
        exit(1)
    
    print(f"Deploying to {environment} environment...")
    # Deployment logic here

# Usage in CI/CD:
# export DEPLOYMENT_KEY=secret_key_value
# python deploy.py production
```

---

## Assignments and Practice

### Assignment 1: Complete Calculator
Extend the calculator example to handle:
- Division operation
- Error handling for division by zero
- Support for more operations (power, modulo)

### Assignment 2: Environment Variable Practice
Create a script that:
- Reads database credentials from environment variables
- Validates all required variables are present
- Simulates database connection

### Assignment 3: Mixed Usage
Build a deployment script that uses:
- Command line arguments for environment selection
- Environment variables for sensitive keys
- Function-based architecture

---

## Key Takeaways

1. **Never hardcode values** in production scripts
2. **Use command line arguments** for user inputs and configuration
3. **Use environment variables** for sensitive information
4. **Convert string arguments** to appropriate data types
5. **Import required modules** (`sys` for args, `os` for env vars)
6. **Plan for security** when handling sensitive data in DevOps workflows

## Next Steps
- Practice with the provided examples
- Convert your Day 4 programs to use command line arguments
- Experiment with environment variables in your development environment
- Think about how these concepts apply to your current DevOps tools and workflows

---

*Remember: As DevOps engineers, we frequently work with CLI tools and need to handle sensitive information securely. These concepts are fundamental to writing robust, secure automation scripts.*
