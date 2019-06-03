print('My name is')
for i in range(5):
    # First time this is run, i is set to 0
    # The for statement is incrementing i by 1 each time for 5x
    # range is a function that can be called with multiple arguments (see below)
    print('Jimmy Five Times ' + str(i))

# Example with a specific range
for i in range(12, 16):
    print('Jimmy Five Times ' + str(i))

# Example with a step argument
for i in range(0, 10, 2):
    print('Jimmy Five Times ' + str(i))
