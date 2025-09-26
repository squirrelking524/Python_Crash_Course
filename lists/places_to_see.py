# Creating list of 5 places I want to visit
five_places = ["London", "Spain", "Germany", "Mexico", "Italy"]
print(five_places)

# Alphabetically sorting list
sorted_places = sorted(five_places)
print(sorted_places)

# Shows still original
print(five_places)

# Return reverse alphabetical order
reverse_sorted_places = sorted(five_places, reverse=True)
print(reverse_sorted_places)

# Shows still original
print(five_places)

# Reversed to original order
five_places.reverse()
print(five_places)

# Curious if it stayed in reverse order = it does
print(five_places)

# Reversed back to original order
five_places.reverse()
print(five_places)

# Alpabetized using sort
five_places.sort()
print(five_places)

# Used sort to reverse alphabetize
five_places.sort(reverse=True)
print(five_places)

print(f"The total number of places I want to go to are: {len(five_places)}")