# This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')
myName = input()
print('It\'s good to meet you, ' + myName + '!')
print('I like when people have names that are ' + str(len(myName)) + ' letters!')
print('How old are you?')
myAge = input()
print('Wow. Thankfully you aren\'t ' + str(int(myAge)+1) + '!')