# dict of three major rivers and their countries

major_rivers = {'nile': 'egypt', 'amazon': 'Brazil', 'yangtze': 'china'}

for river, country in major_rivers.items():
    print(f"\nThe {river.title()} flows through {country.title()}.")

# loop through rivers
print("\nRivers:")
for river in major_rivers.keys():
    print(f"{river.title()}")

# loop through countries
print("\nCountries:")
for country in major_rivers.values():
    print(f"{country.title()}")