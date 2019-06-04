# Global and local scopes
# A variable inside a function can have a different value than outside the function
# Global scope is created when the program runs and is destroyed when it ends
# Local scope is created when the function is called and destroyed when it returns
# Local scope is temporary
# Code in the global scope can't access local variables
# Code in the local scope CAN access global variables
# Code in one local scope cannot use variables in another local scope
# You can use the same name in a local and variable scope, this isn't good practice

spam = 42 # global variable
def eggs():
    spam = 40 # local variable

# Assignment statement in local = local variable
# No assignment statement in local = global variable
def spam2():
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam2()
print(eggs)

# If you want to refer to global eggs
def spam3():
    global eggs # overrides the following local variable
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam3()
print(eggs)
