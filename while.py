# 7-4 Pizza toppings
'''
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nType 'quit' when you are finished "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

    if message != 'quit':
        print(message)
'''

# 7-5 Movie Tickets

prompt = "How old are you to watch this movie? "

while True:
    message = int(input(prompt))

    if message < 3:
        print("Your ticket is free")
    elif message > 3 and message < 12:
        print("Your ticket is $10.00")
    elif message > 12:
        print("Your ticket is $15.00")
    break

'''
# Project to work on

movie_tickets_total = {}

while True:
    prompt_age = int(input("Enter total number of tickets: "))

    for total in range(prompt_age):
        key = input("Enter name: ")
        age = int(input("Enter age: "))
        movie_tickets_total[key] = int(age)
    break

print({key: int(age) if age and '.' not in age else float (age) if age else None
       for key, age in mt.items()}
        for mt in movie_tickets_total)

if age < 3:
    print(f"{key}, since your age is {age}, your ticket is free.")
elif age >= 3 and age < 12:
    print(f"Since your age is {age}, your ticket is $10.")
elif age >= 12:
    if age > 120:
        print("You are not real.")
    else:
        print(f"Since your age is {age}, your ticket is $15.")

'''