# Conditional Statements in Python

Conditional statements are a fundamental part of programming that allow you to make decisions and execute different blocks of code based on certain conditions. In Python, you can use `if`, `elif` (short for "else if"), and `else` to create conditional statements.

## `if` Statement

The `if` statement is used to execute a block of code if a specified condition is `True`. If the condition is `False`, the code block is skipped.

```python
if condition:
    # Code to execute if the condition is True
```

- Example:

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

## `elif` Statement

The `elif` statement allows you to check additional conditions if the previous `if` or `elif` conditions are `False`. You can have multiple `elif` statements after the initial `if` statement.

```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
elif condition3:
    # Code to execute if condition3 is True
# ...
else:
    # Code to execute if none of the conditions are True
```

- Example:

```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is not greater than 5")
```

## `else` Statement

The `else` statement is used to specify a block of code to execute when none of the previous conditions (in the `if` and `elif` statements) are `True`.

```python
if condition:
    # Code to execute if the condition is True
else:
    # Code to execute if the condition is False
```

- Example:

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```
## Best practices 

## 1. use descriptive values 

# Good
instance_type = sys.argv[1]
if instance_type == "t2.micro":
    print("Micro instance selected")

# Avoid
t = sys.argv[1]
if t == "t2.micro":
    print("Micro instance selected")

## 2. Handle the edge cases 

if condition1:
    # Handle condition1
elif condition2:
    # Handle condition2


## 3. keep conditions readable and simple 

# Good
if server_status == "running" and cpu_usage < 80:
    print("Server is healthy")

# Less readable
if server_status == "running" and cpu_usage < 80 and memory_usage < 90 and disk_usage < 85:
    print("Server is healthy")


Interview Questions & Concepts
Q1: What's the difference between = and == in Python?

Q2: Can you have multiple conditions in a single if statement?

    if instance_type == "t2.micro" and region == "us-east-1":
        print("Valid configuration")

Q3: What happens if none of the conditions in if-elif chain are met?

Conditional handling is essential for:

Decision Making: Execute different code paths based on conditions
Validation: Check user inputs and system states
Error Handling: Manage different scenarios gracefully
DevOps Automation: Create intelligent scripts that adapt to different environments