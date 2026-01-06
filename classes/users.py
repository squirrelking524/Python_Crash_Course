class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, you entered your age to be {self.age}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}, it is a pleasure to meet you and thank you for creating an account!")

first_user = User('David', 'Smith', 34)
second_user = User('Alycia', 'Smith', 33)

first_user.describe_user()
first_user.greet_user()

second_user.describe_user()
second_user.greet_user()