from pathlib import Path
import json

fav_num = input("What is your favorite number? ")

path = Path("favorite_num.txt")
contents = json.dumps(fav_num)
path.write_text(contents)

print(f"We have stored your favorite number: {fav_num}")