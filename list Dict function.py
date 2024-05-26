#Demonstrate List and Dictionary with its important function (minimum 3)

# List demonstration
my_list = [1, 2, 3, 4, 5]

# Append: Add element to the end
my_list.append(6)
print("List after appending 6:", my_list)

# Pop: Remove and return last element
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after popping:", my_list)

# Index: Find the index of the first occurrence of an element
index_of_3 = my_list.index(3)
print("Index of 3:", index_of_3)



# Dictionary demonstration
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Get: Retrieve value associated with a key
value_b = my_dict.get('b')
print("Value associated with 'b':", value_b)

# Update: Merge dictionaries or add new key-value pairs
my_dict.update({'d': 4})
print("Dictionary after updating:", my_dict)

# Keys: Retrieve all keys in the dictionary
keys = my_dict.keys()
print("Keys in the dictionary:", keys)

