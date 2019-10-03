#! Занятие по книге Python Crash Course, chapter 8, "Functions".
# Занятие второе.  Return,


def get_formatted_name(first, last, middle=''):
    """Return a full name, neatly formatted."""
    if middle:
        return first.title() + ' ' + middle.title() + ' ' + last.title()
    return first.title() + ' ' + last.title()


print(get_formatted_name('jimi', 'hendrix'))
print(get_formatted_name('john', 'hooker', 'lee'))


def build_person(first_name, last_name, age=''):    # Returning a dictionary.
    """Return a dictionary of information about a person."""
    if age:
        return {'first': first_name, 'last': last_name, 'age': age}
    return {'first': first_name, 'last': last_name}


print(build_person('jimi', 'hendrix'))
print(build_person('serj', 'diforverri', 27))


while True:
    print("\nPlease tell me your nmae:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    full_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + full_name + "!")
    question = input('Do you want to stop it? ')
    if question == 'yes':
        break


def city_country(city, country):
    """Try it yourself 8-6.  City names."""
    return city.title() + ", " + country.title()


print(city_country('moscow', 'russia'), city_country('montreal', 'canada'),
      city_country('santiago', 'chile'))


def make_album(artist, album, tracks=""):
    """Try it yourself 8-7.  Album."""
    if tracks:
        return {'artist': artist, 'album': album, 'tracks': tracks}
    return {'artist': artist, 'album': album}


print(make_album('2pac', '2pacalypse Now'), make_album('ridj', 'assfuck'),
      make_album('system of a down', 'steel this album!', 16))

# Try it yourself 8-8.  User albums.
while True:
    artist = input("Name of artist: ")
    album = input("Name of album: ")
    tracks = input("Number of tracks (optional): ")
    if tracks:
        result = make_album(artist, album, tracks)
    else:
        result = make_album(artist, album)
    print(result)
    question = input("Print yes to quit. ")
    if question == 'yes':
        break
