# Error handling

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError: # Skips over the zero division error
    # except:                 # this also works without definining the exact error 
        print('Error: Division by 0.') # prints the message

print(div42by(2))
print(div42by(12))
print(div42by(0)) # Normally causes an error for dividing by 0, crashes
print(div42by(1)) # Performed because there is an except above
