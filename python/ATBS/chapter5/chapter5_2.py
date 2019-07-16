# Dictionaries vs. Lists

# Items in dictionaries are unordered (unlike lists)
spam = ['cats', 'dogs', 'moose']
bacon = ['moose', 'cats', 'dogs']
print(spam == bacon)

spam = {1: 'cats', 2: 'dogs', 3: 'moose'}
bacon = {3: 'moose', 1: 'cats', 2: 'dogs'}
print(spam == bacon)
