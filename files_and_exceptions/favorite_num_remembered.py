from pathlib import Path
import json

# path = Path("favorite_num.txt")
path = Path("new_favorite_num.txt")
if path.exists():
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f"Your favorite number is: {fav_num}")
else:
    fav_num = input("What is your favorite number? ")
    contents = json.dumps(fav_num)
    path.write_text(contents)
    print(f"We have stored your favorite number: {fav_num}")

