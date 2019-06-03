# name = 'Bob'
name = input()
    # Truthy vs. Falsey values
    # A blank input here would be a Falsey value
    # Anything you type in would be a Truthy value
    # Typically, you want to be more explicit than relying on this
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')

# The order of the following elif statements matters, it will enter the first Block and perform, skipping the rest.
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire')
elif age > 100:
    print('You are not Alice, granny.')
else:
    print('Go away!')
