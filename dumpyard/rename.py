from os import listdir, rename, walk, getcwd, chdir


def get_ind(ind):
    return '%.2d.' % ind

def many_folders(index, path='', file_type='.mp3'):
    folders = next(walk(getcwd()))[1]
    for folder in folders:
        chdir(folder)
        inside_folders = next(walk(getcwd()))[1]
        if len(inside_folders):
            index = many_folders(index, path, file_type)
        index = one_folder(index, path, file_type)
        chdir('..')
    return index
        #rename(, 'files\\' + get_ind() + file)

def one_folder(index, path='', file_type='.mp3'):
    files = listdir()
    for file in files:
        if file_type in file:
            name = path + get_ind(index) + file
            rename(file, name)
            index += 1
    return index

print('Next index is: %d' % many_folders(1, '.mp3'))
