# list of my 3 favorite pizzas
fav_pizzas = ["pepperoni", "meat lovers", "bbq chicken", "taco", "blt"]

'''for pizza in fav_pizzas:
    print(f"I really like {pizza} pizza")'''

'''print(f"I really love pizza. My favorite pizza of all is {fav_pizzas[0]} pizza.")
print(f"My second, usually go to pizza, is {fav_pizzas[1]} pizza.")
print(f"Lastly, when I'm in the mood, I go for {fav_pizzas[2]} pizza. I really love pizza.")

print(f"The first three items in this list are: {", ".join(fav_pizzas[:3])} pizzas")
print(f"The three items from the middle of the list are: {", ".join(fav_pizzas[1:4])} pizzas.")
print(f"The last three items in the list are: {", ".join(fav_pizzas[2:5])} pizzas.")'''


# copying list to make a friends list
friend_pizzas = fav_pizzas[:]

# adding different pizzas to each list
fav_pizzas.append("chicken bacon")
friend_pizzas.append("cheese")

'''print("My favorite pizzas are: ")
for pizza in fav_pizzas:
    print(pizza)

print("My friends favorite pizzas are: ")
for pizzas in friend_pizzas:
    print(pizzas)'''

for favorite in fav_pizzas:
    print(favorite)

for friend in friend_pizzas:
    print(friend)