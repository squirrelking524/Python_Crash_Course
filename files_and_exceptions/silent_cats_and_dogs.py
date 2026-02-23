from pathlib import Path

def pet_names(filename):
    try:
        contents = path.read_text()
    except:
        pass
    else:
        print(f"These are the pet names: \n{contents.rstrip()}")

files = ['dogs.txt', 'cats.txt']

for filename in files:
    path = Path(filename)
    pet_names(path)