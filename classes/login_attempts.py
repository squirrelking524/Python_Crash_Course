class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.login_attempts = 0
        

    def describe_user(self):
        print("\nYour user info is listed below:")
        print(f"{self.first_name} {self.last_name}, you entered your username to be {self.username}")
        print(f"{self.username}, your email for your account is: {self.email}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}, username: {self.username}, it is a pleasure to meet you and thank you for creating an account!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

first_user = User('David', 'Smith', 'davidlsmith21', 'davidlsmith524@gmail.com')
second_user = User('Alycia', 'Smith', 'aly2025', 'alycia@yahoo.com')

first_user.describe_user()
first_user.greet_user()

print("\nMaking 3 login attempts...")
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
print(f"Your login attempts: {first_user.login_attempts}")

print("\nResetting your login attempts")
first_user.reset_login_attempts()
print(f"\nYour login attempts are now: {first_user.login_attempts}")


second_user.describe_user()
second_user.greet_user()