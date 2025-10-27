# dictionary of person's info
'''
alycia = {'first_name': 'Alycia', 'last_name': 'Smith', 'age': '34', 'city': 'Columbus'}

print(f"Your first name is: {alycia['first_name']}.")
print(f"Your last name is: {alycia['last_name']}.")
print(alycia['age'])
print(alycia['city'])

# favorite numbers of 5 different people

fav_nums = {'Larry': '69', 'David': '7', 'Alycia': '19', 'Nora': '8', 'Emebet': '28'}

print(f"Larry, your favorite number is {fav_nums['Larry']}.")
print(f"David, your favorite number is {fav_nums['David']}.")
print(f"Alycia, your favorite number is {fav_nums['Alycia']}.")
print(f"Nora, your favorite number is {fav_nums['Nora']}.")
print(f"Emebet, your favorite number is {fav_nums['Emebet']}")'''

# glossary of five new terms I've learned about

glossary = {
    'variable': 'Every variable is connected to a value, which is the information associated with that variable',
    'string': 'Anything inside quotes is considered a string',
    'loop': 'An automated task a computer runs repetitive tasks',
    'tuple': 'An immutable list',
    'boolean': 'A Boolean value is either True or False',
    }

'''print(f"Variable: \n{glossary['variable']}")
print(f"String: \n{glossary['string']}")
print(f"Loop: \n{glossary['loop']}")
print(f"Tuple: \n{glossary['tuple']}")
print(f"Boolean: \n{glossary['boolean']}")'''

#quicker way to loop through dicitionary
for term, definition in sorted(glossary.items()):
    print(f"\n{term.title()}:")
    print(f"{definition}")