from city_country import city_and_country

def test_city_and_country():
    formatted_cities = city_and_country('santiago', 'chile')
    assert formatted_cities == "Santiago, Chile"