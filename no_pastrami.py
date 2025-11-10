sandwich_orders = ['turkey', 'pastrami', 'ham', 'pastrami', 'pastrami', 'meatball', 'steak and cheese', 'pastrami']
finished_sandwiches = []

print('We are sorry, we ran out of Pastrami!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    ordered_sandwich = sandwich_orders.pop()
    print(f'We are currently finishing up your {ordered_sandwich.title()} sandwich!')

    finished_sandwiches.append(ordered_sandwich)