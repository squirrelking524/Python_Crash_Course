# Storing dictionaries inside of a list

alycia = {'first_name': 'Alycia', 'last_name': 'Smith', 'age': '34', 'city': 'Columbus'}

larry = {'first_name': 'Larry', 'last_name': 'Parks', 'age': '22', 'city': 'Columbus'}

david = {'first_name': 'david', 'last_name': 'smith', 'age': '34', 'city': 'altoona'}

people = [alycia, larry, david]

# looping through list
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nFullname: {full_name.title()}")
    print(f"Age: {person['age']}")
    print(f"Birthplace: {person['city']}")


# Storing dictionaries inside of list for pets
'''
dakota = {'owner': 'dave smith', 'kind': 'dog', 'pet_name': 'dakota'}

buckeye = {'owner': 'jeff andsherri', 'kind': 'dog', 'pet_name': 'buckeye'}

nala = {'owner': 'david and alycia', 'kind': 'dog', 'pet_name': 'nala'}

pets = [dakota, buckeye, nala]

for pet in pets:
    print(pet)
    '''
'''
# Dicitionary for favorite places

favorite_places = {
    'jason':['italy', 'rome'],
    'alycia': ['europe', 'disney'],
    'emebet': ['africa', 'ethiopia']
}

for person,place in favorite_places.items():
    print(f"{person.title()}'s favorite place is {' and '.join(place)}.")
    '''