# Infinite loop program with continue
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
        # continue sends you back to the top of the loop to reevaluate the condition
        # On the 3rd loop through continue skips the print function back to the top of the loop
    print('spam is ' + str(spam))
