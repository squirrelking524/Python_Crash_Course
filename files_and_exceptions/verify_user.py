from pathlib import Path
import json

path = Path('username.json')
def get_stored_user(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_user(path):
    username = input("What is your username? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
    
# My original    
def correct_user(path):    
    username = get_stored_user(path)
    question_user = input(f"Is this your correct username: {username} (y/n)? ")
    if question_user.lower() == 'y':
        greet_user()
    else:
        username = get_new_user(path)
        print(f"We will remember you next time you are back, {username}")

def greet_user():
    username = get_stored_user(path)
    # inspired by other user by using 2 if statments
    if username:
        print(f"Welcome back, {username}")
        '''
        correct_user = input(f"Is this your username: {username}? (y/n) ")
        if correct_user.lower() == 'y':
            print(f"Welcome back, {username}")
        else:
            username = get_new_user(path)
            print(f"We will remember you next time you are back, {username}")
            '''
    else:
        username = get_new_user(path)
        print(f"We will remember you next time you are back, {username}")

correct_user(path)