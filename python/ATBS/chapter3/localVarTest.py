# This will print 42 twice because the function refers to the global variable as well.

def spam():
    print(eggs)

eggs = 42
spam()
print(eggs)