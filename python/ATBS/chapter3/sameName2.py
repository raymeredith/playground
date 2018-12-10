def spam():
    global eggs # eggs is declared global, so the assignment is done to the global eggs even though it's performed locally.
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)