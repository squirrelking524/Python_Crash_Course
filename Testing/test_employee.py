from employees import Employee

def test_employees():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    annual_salary = input("What is your annual salary? ")
    employees = Employee(first_name, last_name, annual_salary)
    assert 'david', 'smith' '9' in employees.employee_info

'''
    employees = Employee(first_name, last_name, annual_salary)

    employees.employee_info()
'''
