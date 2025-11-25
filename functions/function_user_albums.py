def make_album(name, title):
    record = f"Artist name:{name}; Album Title:{title}"
    return record

while True:
    print("\nWhat is your favorite musical artist and album title?")
    a_name = input("Artist name: ")
    a_title = input("Album title: ")

    album = make_album(a_name, a_title)
    print(f"\nYour favorite artist and album is: {album}")