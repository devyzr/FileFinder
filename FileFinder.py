from os import listdir
from os.path import isfile, sep, join


# Gets the files of a directory, if no directory is passed gets root dir
def get_files(path='', extension=''):
    only_files = []
    if(path):
        files = listdir(path)
    else:
        files = listdir()

    for f in files:
        if(path):
            f = join(path, f)
        # Checks if it's a file
        if isfile(f):
            str_f = str(f)
            # Check for extension if specified, if not we append the file
            if(extension):
                ext = str_f.split('.')
                ext = ext[-1]
                if extension == ext:
                    only_files.append(f)
            else:
                only_files.append(f)

    return only_files


# Gets the directories in a path, if no directory is passed gets root dir
def get_dirs(path=''):
    only_dirs = []
    if(path):
        files = listdir(path)
    else:
        files = listdir()

    for f in files:
        if(path):
            f = join(path, f)
        # Checks if it's a file, if not appends to directories
        if not isfile(f):
            only_dirs.append(f)

    return only_dirs


# Get all the files in current or specified path
def get_all_files(path='.', extension=''):
    files = []
    dirs = []

    for item in listdir(path):
        full_path = path + sep + item
        dirs.append(full_path)

    while dirs:
        elem = dirs.pop()

        if isfile(elem):
            if extension:
                ext = elem.split('.')[-1]
                if ext == extension:
                    files.append(elem)
            else:
                files.append(elem)
        else:
            more_dirs = listdir(elem)
            for e in more_dirs:
                full_path = elem + sep + e
                dirs.append(full_path)

    return files


# Get all the files in current or specified path
def get_all_dirs(path='.'):
    files = []
    dirs = []

    for item in listdir(path):
        full_path = path + sep + item
        files.append(full_path)

    while files:
        elem = files.pop()

        if not isfile(elem):
            dirs.append(elem + sep)
            more_dirs = listdir(elem)
            for e in more_dirs:
                full_path = elem + sep + e
                files.append(full_path)

    return dirs
