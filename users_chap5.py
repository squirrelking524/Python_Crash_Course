# greeting users and admin
'''
usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello, {user}, thank you for logging in again')
else:
    print('We need to find some users!')'''

# checking for unique usernames
current_users = ['Chris', 'Alpha', 'Rose', 'David', 'Jason']
new_users = ['Andrew', 'ALPHA', 'Emebet', 'Nick', 'DaVid']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'{new_user}, you need to choose a new username')
    else:
        print(f'{new_user}, that username is available')