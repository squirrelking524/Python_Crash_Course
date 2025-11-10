responses = {}

poll_active = True

while poll_active:
    name = input('\nWhat is your name? ')
    prompt = input('If you could visit one place in the world, where would you go? ')

    responses[name] = prompt

    repeat = input('Is there anyone else taking the survey? (yes/no) ')
    if repeat == 'no':
        poll_active = False

print('\n---Survey Results---')
for name, prompt in responses.items():
    print(f'{name.title()}, would like to go to {prompt.title()}')