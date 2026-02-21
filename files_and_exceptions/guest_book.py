from pathlib import Path

while True:
    guest_need = input("Are you still adding guests? (y/n) ")

    if guest_need == "n":
        break

    else:
        guest_book = ""

        guest_book += input("What is your guest name? ")
    
        guest_book += "\n"

path = Path('guest_book.txt')
path.write_text(guest_book)