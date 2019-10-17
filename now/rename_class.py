import os
from os import listdir, rename, walk, getcwd, chdir

class Renamer:
    def __init__(self):
        self.index = 1
        self.index_length = '%.2d'
        self.file_type = '.mp3'
        self.replacer = None
        self.addition = None
        self.path = None

    def get_index(self):
        return self.index_length % self.index

    def set_index_length(self, length):
        self.index_length = '%.' + str(length) + 'd'

    def set_file_type(self, file_type):
        self.file_type = '.' + file_type

    def reset_index(self):
        self.index = 1

    def set_index(self, index):
        self.index = index

    def set_addition(self, addition):
        self.addition = addition

    def set_replacer(self, replacer):
        self.replacer = replacer

    def rename_files(index=self.index, file_type=self.file_type, path=self.path, replacer=self.replacer, addition=self.addition):
        files = os.listdir()
        for file in files:
            if file_type in file:
                name = path + self.get_index(index) + (addition or '') + (replacer or file)
                rename(file, name)
            index += 1
        self.index = index
    return index


a = Renamer()
print(a.get_index())


def get_ind(ind):
    return '%.2d.' % ind

def many_folders(index, file_type='.mp3'):
    folders = next(walk(getcwd()))[1]
    for folder in folders:
        chdir(folder)
        inside_folders = next(walk(getcwd()))[1]
        if len(inside_folders):
            index = many_folders(index, file_type)
        index = one_folder(index, file_type)
        chdir('..')
    return index
        #rename(, 'files\\' + get_ind() + file)

def one_folder(index, file_type='.mp3'):
    files = listdir()
    for file in files:
        if file_type in file:
            name = 'C:\\_td\\muz_medieval\\' + get_ind(index) + file
            rename(file, name)
            index += 1
    return index

#print('Next index is: %d' % many_folders(1, '.mp3'))
