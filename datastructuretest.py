my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)

# Extend the list with another list
my_list.extend([50, 60, 70])

# Print the final list
print(my_list)
# Remove the last element from the list
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find the index of the value 30
index_of_30 = my_list.index(30)

# Print the sorted list and the index of 30
print("Sorted list:", my_list)
print("Index of 30:", index_of_30)
