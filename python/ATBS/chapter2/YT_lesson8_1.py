# Standard library are modules with various functions
# Need to import these modules to use them

import random
number = random.randint(1, 10)
# Needs to start with random. to tell it to look in the random module for the function
# randint() is a function in the random module
print(number)

# Example of importing multiple modules at once
import sys, os, math

# Import everything from random
# If used, you don't need to specify random before the function
# It's good practice to still use it though for clarity
from random import *
randint(1, 10)

# sys was imported above in line 11
print('Hello')
sys.exit()
print('Goodbye') # This wont be printed
