'''
rental_car = input("What type of rental car would you like? ")

print(f"Let me see if I can find you a {rental_car}")
'''

seating = input("How many are in your dinner party? ")

seating = int(seating)

if seating > 8:
    response = input("Your table will be avilable in 1 hour. Is that okay? ")
    if response.lower() == "yes":
        print("Your table will be ready in 1 hour!")
    else:
        print("We are sorry to see you go!")
else:
    print("Your table will be ready soon!")