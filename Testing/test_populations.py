from populations import city_country_population

def test_city_country_population():
    formatted = city_country_population('santiago', 'chile', 5000)
    assert formatted == "Santiago, Chile - Population 5000"