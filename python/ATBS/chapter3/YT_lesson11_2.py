# Error handling

# An input that isn't a number (i.e. "six") which is turned to an integer will error
# Need to use an except to get past the error

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That\'s a lot of cats.')
    elif int(numCats) < 0:
        print('You can\'t have a negative amount of cats.')
    else:
        print('That\'s not that many cats')
except:
    print("You did not enter a number.")
