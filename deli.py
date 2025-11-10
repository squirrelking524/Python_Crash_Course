sandwich_orders = ['turkey', 'ham', 'meatball', 'steak and cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"We are finishing your {current_sandwich.title()} sandwich!")

    finished_sandwiches.append(current_sandwich)

