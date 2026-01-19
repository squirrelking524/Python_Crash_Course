class User:
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        print(f"    Username: {self.username}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}, it is a pleasure to meet you and thank you for creating an account!")

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = []
    
    def show_privileges(self):
        print('\nPrivileges:')
        for privilege in self.privileges:
            print(f'- {privilege}')

david = Admin('david', 'smith', 'dls000')
david.describe_user()

david.privileges = [
    'can change passwords',
    'can assign new users',
    'can remove users'
]

david.show_privileges()