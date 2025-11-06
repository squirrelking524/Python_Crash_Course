# 6-7 Storing dictionaries inside of a list
'''
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
'''

# 6-8 Storing dictionaries inside of list for pets
'''
dakota = {'owner': 'dave smith', 'kind': 'dog', 'pet_name': 'dakota'}

buckeye = {'owner': 'jeff andsherri', 'kind': 'dog', 'pet_name': 'buckeye'}

nala = {'owner': 'david and alycia', 'kind': 'dog', 'pet_name': 'nala'}

pets = [dakota, buckeye, nala]

for pet in pets:
    print(pet)
    '''
'''
# 6-9 Dicitionary for favorite places

favorite_places = {
    'jason':['italy', 'rome'],
    'alycia': ['europe', 'disney'],
    'emebet': ['africa', 'ethiopia']
}

for person,place in favorite_places.items():
    print(f"{person.title()}'s favorite place is {' and '.join(place)}.")
    '''

# 6-10 Printed mulitiple favorite numbers for different people
'''
fav_nums = {
    'Larry': ['69', '89'],
    'David': ['7', '19'], 
    'Alycia': '19', 
    'Nora': '8', 
    'Emebet': '28'
}

for person, nums in fav_nums.items():
    print(f"\n{person}'s favorite numbers are {' and '.join(nums)}")
'''

# 6-11 Cities and their info 

cities = {
    'columbus': {
        'state': 'ohio',
        'population': '2,358',
        'govenor': 'dewine',
    },

    'pittsburgh':{
        'state': 'pennsylvania',
        'population': '5,681',
        'govenor': 'smith',
    },
}

for city, city_info in cities.items():
    govenor = f"{city_info['govenor']}"
    state = f"{city_info['state']}"
    print(f"\nThe following city, {city.title()}, is located in the state of {state.title()}, with a population of {city_info['population']} and their govenor is {govenor.title()}.")
