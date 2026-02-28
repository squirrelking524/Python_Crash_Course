def city_country_population(city, country, population = ''):
    if population:
        CityCountryPopulation = f"{city}, {country} - population {population}"
    else:
        CityCountryPopulation = f"{city}, {country}"    
    return CityCountryPopulation.title()