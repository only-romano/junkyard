# Копирование файла по пути

def copy_file(way, name):
    old_file = open(way)
    text = old_file.read()
    old_file.close()
    new_file = open(name, 'w')
    new_file.write(text)
    new_file.close()


if __name__ == '__main__':
    copy_file("test.txt", "copy_test.txt")
