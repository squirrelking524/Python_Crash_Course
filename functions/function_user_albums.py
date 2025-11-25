def make_album(name, title):
    record = f"Artist name: {name.title()}; Album Title: {title.title()}"
    return record

while True:
    print("\nWhat is your favorite musical artist and album title?")
    print("(enter 'q' at any time to quit)")
    a_name = input("Artist name: ")
    if a_name == 'q':
        break
    a_title = input("Album title: ")
    if a_title == 'q':
        break

    album = make_album(a_name, a_title)
    print(f"\nYour favorite artist and album is: {album}")