def make_album(name, title, songs=None):
    album = {'artist name': name, 'album title': title}
    if songs:
        album['songs'] = songs
    return album

record = make_album('Andrew Best', 'Turkey Day')
print(record)

record = make_album('Andrew Best', 'Crazy Cat!!!')
print(record)

record = make_album('Andrew Best', 'Emerson the Moose', 13)
print(record)