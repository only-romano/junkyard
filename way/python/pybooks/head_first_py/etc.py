# Various stuff from the book
# diy 1
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
for i in range(3):
    movies.insert(1 + i*2, 1975 + i*4)

print(movies)


# diy 2
try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(f"{role} said: {line_spoken}", end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print("The data file is missing!")


# diy 4
import sys

def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)
            print(each_item, file=fh)


# diy 3
man = []
booka = []

try:
    with open('sketch.txt', 'r') as file:
        for each_line in file:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Booka':
                    booka.append(line_spoken)
            except ValueError:
                pass
except IOError:
    print("The datafile is missing")

try:
    man_file = open('man_data.txt', 'w')
    booka_file = open('booka_data.txt', 'w')
    print_lol(man, fh=man_file)
    print_lol(booka, fh=booka_file)
except IOError as err:
    print(f"File error: {err}")
finally:
    if 'man_file' in locals():
        man_file.close()
    if 'booka_file' in locals():
        booka_file.close()
