# passing IF test
alien_color = 'green'

if alien_color == 'green':
    print('You just earned 5 points!') 
elif alien_color == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')

# second passing IF test that passes else statement
alien_color = 'yellow'

if alien_color == 'green':
    print('You just earned 5 points!') 
elif alien_color == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')

# third passing IF test
alien_color = 'red'

if alien_color == 'green':
    print('You just earned 5 points!') 
elif alien_color == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')

# failed IF test
'''alien_color = 'yellow'

if alien_color == 'red':
    print('You just earned 5 points!')'''

# person's stage of life IF statements

age = 4

if age < 2:
    print('You are still just a baby')
elif age >= 2 and age < 4:
    print('You are just a toddler')
elif age >= 4 and age < 13:
    print('You are just a kid')
elif age >= 13 and age < 20:
    print('You are just a teenager')
elif age >= 20 and age < 65:
    print('You are an adult')
elif age >= 65:
    print('You are an elder')
