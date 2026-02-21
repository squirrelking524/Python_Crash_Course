from pathlib import Path

path = Path('guest_book.txt')

print("When you have completed the guest book, type: 'quit'.")
while True:
    name = input("What is your name? ")
    if name.lower() == 'quit':
        break

    else:
        with open(path, 'a') as f:
            f.write(f"{name}\n")
        print(f"{name} has been added to the guest book.")