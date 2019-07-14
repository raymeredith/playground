# Ranges and list-like value
print(list(range(4)))

# Can use range and list to more easily add a lot of values to a list
spam = list(range(0, 100, 2))
print(spam)

# Using loop code over a list
# List can be any size and the code will still work to print index
supplies = ['pencils', 'staplers', 'flamethrowers', 'pens', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# Multiple Assignment
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
# Or you can use multiple assignment and do the same thing with one line
size, color, disposition = cat

# Variable swapping
a = 'AAA'
b = 'BBB'
a, b = b, a # swaps the variables
print(a)
print(b)

# Augmented assignment operators
spam = 42
spam += 1 # this takes variable spam and adds 1 to it
print(spam)
