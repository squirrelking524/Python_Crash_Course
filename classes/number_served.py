class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves wonderfully made {self.cuisine_type}")
    
    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, served):
        self.number_served += served


restaurant = Restaurant('uncle beths', 'bbq')
restaurant.describe_restaurant()

print(f"Number of customers served: {restaurant.number_served}")
restaurant.number_served = 200
print(f"Number of customers served: {restaurant.number_served}")

restaurant.number_served = 500
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(300)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(50)
print(f"Numbered served for the day has caused an increase to: {restaurant.number_served}")