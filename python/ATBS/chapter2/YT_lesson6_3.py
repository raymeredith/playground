# Infinite loop program with break
name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
        # This breaks out of the loop and continue with program below
print('Thank you!')