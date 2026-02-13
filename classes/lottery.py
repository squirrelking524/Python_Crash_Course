# generate lottery ticket

from random import choice

lottery_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("Today's winning lottery ticket is...")

while len(winning_ticket) < 4:
    pulled_item = choice(lottery_values)
    
    # allows for repeating values
    winning_ticket.append(pulled_item)

"""
    # doesn't allow for repeating values
    if pulled_item not in winning_ticket:
        print(f" We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)
        """

print(f"The final winning ticket is: {winning_ticket}")