from random import choice

def get_winning_ticket(lottery_values):
    winning_ticket = []

    while len(winning_ticket) < 4:
        pulled_item = choice(lottery_values)
        winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(my_ticket, winning_ticket):
    if my_ticket == winning_ticket:
        return True
    else:
        return False

'''
def make_random_ticket(lottery_values):
    ticket = []

    while len(ticket) < 4:
        pulled_item = choice(lottery_values)
        ticket.append(pulled_item)

    return ticket
'''


lottery_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(lottery_values)
ticket = [1, 2, 3, 4]

plays = 0
won = False

max_tries = 1_000_000

'''
while not won:
    new_ticket = make_random_ticket(lottery_values)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It took only {plays} to win")

else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
'''

while not won:
    won = check_ticket(ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket")
    print(f"Your ticket was: {ticket}")
    print(f"The winning ticket is: {winning_ticket}")
    print(f"It took a total of {plays} to pull your ticket to win!")

else:
    print(f"Tried {plays} times without pulling a winner. :(")
    print(f"Your ticket was: {ticket}")
    print(f"Winning ticket is: {winning_ticket}")