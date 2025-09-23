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
fruits.discard("banana")  # Doesn't raise error if not found
print(f"After removal: {fruits}")

# Set operations (mathematical)
set1 = {"apple", "banana", "orange" , "kiwi", "mango"}
set2 = {"kiwi", "mango", "grape", "pineapple" ,"cherry"}

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



# Frozen set (immutable set)

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