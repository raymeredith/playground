# Lists
# Value that contains values in an ordered sequence = items

# Index
# To access an item in the list, use an integer index

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0]) # will print first item in the list

# Lists can contain lists

spam2 = [['cat', 'dog'], [10, 20, 30]]
print(spam2[0]) # will show the whole first list
print(spam2[0][1]) # will print the 2nd item in the 1st list

# Negative index counts from the end going backwards

spam3 = ['cat', 'bat', 'rat', 'elephant']
print(spam3[-1]) # will print the last item in the list

# Slices
# Gets several values from a list

spam4 = ['cat', 'bat', 'rat', 'elephant']
print(spam4[0:3])

# Use an index to replace a value in a list (works similarly with a slice)
spam5 = [10, 20, 30, 40]
spam5[1] = 'Hello'
print(spam5)

spam6 = ['cat', 'bat', 'rat', 'elephant']
spam6[:2] # Python assumes this means start at the beginning
spam6[1:] # Starts at 1 and returns everything to the end

# Delete item
spam7 = ['cat', 'bat', 'rat', 'elephant']
del spam7[2] # Think of as an unassignment statement
print(spam7)

# Number of items in a list
print(len(spam7)) # Gets the number of items remaining in spam7

# List concatenation: uses normal operators
spam8 = [1, 2, 3]
spam9 = [4, 5, 6]
print(spam8 + spam9)

# List function creates a list of characters passed to it
print(list('Hello'))

# Check to see if something is in a list
print('howdy' in ['hello', 'hi', 'howdy']) # Checks for howdy in the list
print('howdy' not in ['hello', 'hi', 'howdy'])