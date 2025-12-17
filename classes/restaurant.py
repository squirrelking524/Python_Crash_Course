class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name}: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("The restaurant is open.")

restaurant = Restaurant("McDonalds", "Burgers")
print(f"The restaurant {restaurant.restaurant_name} is an American staple.")
print(f"{restaurant.restaurant_name} cuisine type is {restaurant.cuisine_type}")