class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name}: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("The restaurant is open.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def show_flavors(self):
        print("\nWe have the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

bobs = IceCreamStand('Bobs')
bobs.flavors = ['vanilla', 'chocolate', 'strawberry']

bobs.describe_restaurant()
bobs.show_flavors()
