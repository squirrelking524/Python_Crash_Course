class Employee:

    def __init__(self, first_name, last_name, annual_salary = []):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def employee_info(self):
        print(f"Thank you, {self.first_name} {self.last_name} for entering your information and annual salary of {self.annual_salary}") 

    def give_raise(self):
        self.new_salary = self.annual_salary + 5000
        print(f"Your {self.annual_salary} just earned a $5,000 bonus!")
        print(f"Your new salary is {self.new_salary}")