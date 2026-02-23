from pathlib import Path

path = Path('city_of_god.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, we could not find {path}")
else:
    words = contents.lower().count('the')
    print(f"The text '{path}' has the word 'the' appear {words} times.")