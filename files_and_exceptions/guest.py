from pathlib import Path

guest_user = input("Input your name here: ")

print(input)

path = Path("guest.txt")
path.write_text(guest_user)