# keys(), values(), and items() Methods
# These are the 3 dictionary methods
# The methods can't be modified like lists with append()

# Dictionary methods can be used in for loops
# The for loop will iterate over each value, key, or pair in the dictionary
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)

# To get a list from a dictionary method
spam = {'color': 'red', 'age': 42}
print(spam.keys())
print(list(spam.keys()))

# Multiple assignment to assign key and value to separate vars
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))