# favorite languages poll
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# people who should take the pool
poll_takers = ['david', 'edward', 'steve', 'phil']

# printing message thanking those who have taken the poll, and requesting poll takers to take it
for person in favorite_languages.keys() and poll_takers:
    if person in favorite_languages:
        print(f"Thank you, {person.title()} for taking the poll")
    elif person in favorite_languages or poll_takers:
        print(f"{person.title()}, you need to take the poll!")