def city_country(city, country):
    location = f"{city}, {country}"
    return location.title()

area = city_country("Paris", "France")
print(area)