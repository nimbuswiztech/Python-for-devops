# logical operator in python

#Logical and operator (and)

x = True
y = True

result = x and y
print(f"x and y: {result}")  # False, because both x and y need to be True for the result to be True

# Logical or operator (or)

x = 1
y = 0

result = x or y
print(f"x or y: {result}")  # True, because at least one of x

# logical not 

x = False
result = not x
print(f"not x: {result}")  # False, because not True is False



# Alert system using logical operators
cpu_alert = True
memory_alert = False
disk_alert = True
network_alert = False

# Critical alert: both CPU and memory are high
critical_alert = cpu_alert and memory_alert  # False

# Any alert: at least one resource is problematic
any_alert = cpu_alert or memory_alert        # True

# System healthy: no alerts active
system_healthy = not (cpu_alert or memory_alert or disk_alert)  # False

# Multiple conditions
high_priority = (cpu_alert and memory_alert) or disk_alert  # True

print(f"Critical Alert: {critical_alert}")
print(f"Any Alert Active: {any_alert}")
print(f"System Healthy: {system_healthy}")
print(f"High Priority: {high_priority}")


# membership operators

# in
# not in


fruits = ["apple", "banana", "cherry"]
result = "banana" in fruits
print(f"Is 'banana' in fruits? {result}")  # True, because "

#not in 

result = "apple" not in fruits
print(f"Is 'apple' not in fruits? {result}")  # True,


#precedence of operators

result = 5 * 3 + 2  # Multiplication has higher precedence than addition
print(f"Result of 5 + 3 * 2: {result}")  #

result = (5 + 3) * 2  # Parentheses change the order of operations
print(f"Result of (5 + 3) * 2: {result}")

result = not True and False  # 'not' has higher precedence than 'and'
print(f"Result of not True and False: {result}")


# relational operators

#equal to (==)
# not equal to (!=)
# greater than (>)
# less than (<)
# greater than or equal to (>=)
# less than or equal to (<=)


a = 30
b = 40

result = a == b
print(f"a == b: {result}")  # False, because 10 is not equal

result = a != b
print(f"a != b: {result}")  # True, because 10 is not equal

result = a > b
print(f"a > b: {result}")  # False, because 10 is not greater

result = a < b
print(f"a < b: {result}")  # True, because 10 is less than

result = a >= b
print(f"a >= b: {result}")  # False, because 10 is not greater

result = a <= b
print(f"a <= b: {result}")  # True, because 10 is less than

