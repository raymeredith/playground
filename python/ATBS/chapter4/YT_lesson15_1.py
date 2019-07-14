# Methods, and the List Methods: index(), append(), insert(), remove(), sort()
# Method is the same as a function but called on a certain value

# index()
spam = ['hello', 'hi', 'howdy']
print(spam.index('hello')) # will return 0

# append() and insert()
# append() adds to the end of the list, insert() adds at a location in the list
# These are list methods and can't be called on other values like strings and integers
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)

# remove()
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('elephant') # this lets you remove the value wherever in the list, instead of using del on a specific index
print(spam)

# remove() will only remove the first instance of the value in the list
spam = ['cat', 'bat', 'rat', 'elephant', 'cat', 'cat']
spam.remove('cat')
print(spam)

# sort()
# Can't sort a list with both string and integer types
spam = [2, 5, 3.14, -7, 0]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

# Uppercase characters come before lowercase when sorting, "ASCII-betical"
# Uses convert to lower string method and pass to the sort function
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)
