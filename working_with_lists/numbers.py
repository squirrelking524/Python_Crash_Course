# looping through to count to 20
'''for number in range(1, 21):
    print(number)'''

# looping through one-million
'''for num in range(1, 1000000 + 1):
    print(num)'''

# finding min, max, and sum of 1 to one-million
'''numbers = range(1, 1000000 + 1)
print(min(numbers))
print(max(numbers))
print(sum(numbers))'''

# printing odd numbers 1-20
'''odd_nums = list(range(1, 21, 2))
for num in odd_nums:
    print(num)'''

# printing multiples of 3
'''mult_of_three = list(range(3, 30))
for num in mult_of_three:
    mult = (num * 3)
    print(mult)'''

# alternative way: wasn't sure if range was to include multiple of 30 as max, or to get to 30
'''mult_of_three = []
for num in range(3, 10):
    mult_of_three = num * 3
    print(mult_of_three)'''

# cubes of 10
for number in range(1, 11):
    cube = number ** 3
    print(cube)

# comprehensive list
cubed = [value**3 for value in range(1, 11)]
print(cubed)