a = 10 
b = 7 

# Bitwise AND

result = a & b  # 1010 & 0111 = 0010
print(f"Bitwise AND: {result}")

# Bitwise OR
result = a | b  # 1010 | 0111 = 1111
print(f"Bitwise OR: {result}")

# Bitwise XOR
result = a ^ b  # 1010 ^ 0111 = 1101
print(f"Bitwise XOR: {result}")

# Bitwise NOT
result = ~a  # ~1010 = 0101 (in 2's complement)
print(f"Bitwise NOT: {result}")

# Left Shift
result = a << 2  # 1010 << 2 = 1010
print(f"Left Shift: {result}")

# Right Shift
result = a >> 2  # 1010 >> 2 = 0010
print(f"Right Shift: {result}")