from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

'''
lines = contents.splitlines()
for line in lines:
    c = contents.replace('Python', 'C')
'''

for line in contents.splitlines():
    c = contents.replace('Python', 'C')

print(c)