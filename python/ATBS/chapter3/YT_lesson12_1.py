# Guess the number game
import random

print('Hello. What is your name?')

# Checks to make sure the name entered isn't a number
nameCheck = 0
while nameCheck == 0:
    global name
    name = input()
    try:
        if '.' in name:
            print('Your name can\'t be a number!')
            continue
        else:
            val = int(name)
            print('Your name can\'t be a number!')
            continue
    except ValueError:    
        if name == '':
            print('I need a name!')
            continue
        else:
            nameCheck = 1

# Random number picker
minNum = 1
maxNum = 20
secretNumber = random.randint(minNum, maxNum)
print ('Well ' + name + ', I am thinking of a number between ' + str(minNum) + ' and ' + str(maxNum) + '.')

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # Breaks out of this loop with correct number

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed the number in ' + str(guessesTaken) + ' tries!')
else:
    print('Nope! The number I was thinking of was ' + str(secretNumber) + '!')
