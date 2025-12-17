class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name}: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("The restaurant is open.")

mc_donalds = Restaurant("McDonalds", "American/fast-food")
print(f"The restaurant {mc_donalds.restaurant_name} is an American staple.")
print(f"{mc_donalds.restaurant_name} cuisine type is {mc_donalds.cuisine_type}")

olive_garden = Restaurant("Olive Garden", "American/Italian")
print(f"\n{olive_garden.restaurant_name} is a popular Italian themed restaurant in American.")
print(f"Their primary cuisine type is: {olive_garden.cuisine_type}")

uncle_beths = Restaurant("Uncle Beths", "BBQ")
print(f"\n{uncle_beths.restaurant_name} is a small restaurant located just outside North Lewisburg, OH.")
print(f"Their primary cuisine type is: {uncle_beths.cuisine_type}")