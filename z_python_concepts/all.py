# Example 1: Checking a list of booleans
bool_list = [True, True, True]
result = all(bool_list)
print(result)  # Output: True

bool_list = [True, False, True]
result = all(bool_list)
print(result)  # Output: False

# Example 2: Checking if all elements in a list are positive
numbers = [1, 2, 3, 4, 5]
result = all(n > 0 for n in numbers)
print(result)  # Output: True

numbers = [1, 2, -3, 4, 5]
result = all(n > 0 for n in numbers)
print(result)  # Output: False
# Example 3: Checking if all strings in a list are non-empty
strings = ["apple", "banana", "cherry"]
result = all(s for s in strings)
print(result)  # Output: True

strings = ["apple", "", "cherry"]
result = all(s for s in strings)
print(result)  # Output: False

# Example 4: Checking if all values in a dictionary are positive
dictionary = {'a': 1, 'b': 2, 'c': 3}
result = all(value > 0 for value in dictionary.values())
print(result)  # Output: True

dictionary = {'a': 1, 'b': -2, 'c': 3}
result = all(value > 0 for value in dictionary.values())
print(result)  # Output: False

# Example 5: Checking if all elements in nested lists are positive
nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = all(all(n > 0 for n in sublist) for sublist in nested_lists)
print(result)  # Output: True

nested_lists = [[1, 2, 3], [4, -5, 6], [7, 8, 9]]
result = all(all(n > 0 for n in sublist) for sublist in nested_lists)
print(result)  # Output: False

