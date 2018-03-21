from os import listdir, rename
from os.path import isfile, sep


# Gets the files of a directory
def get_files(path='.', extension=''):
    only_files = []

    for item in listdir(path):
        if path[-1] == sep:
            path = path[:-1]
        full_path = path + sep + item

        if isfile(full_path):
            if extension:
                f_ext = item.split('.')
                if f_ext[-1] == extension:
                    only_files.append(full_path)
            else:
                only_files.append(full_path)

    return only_files


# Get all the files in current path and child folders
def get_all_files(path='.', extension=''):
    files = []
    dirs = []

    for item in listdir(path):
        if path[-1] == sep:
            path = path[:-1]
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


# Gets the directories in a path
def get_dirs(path='.'):
    only_dirs = []

    for item in listdir(path):
        if path[-1] == sep:
            path = path[:-1]
        full_path = path + sep + item
        if not isfile(full_path):
            only_dirs.append(full_path)

    return only_dirs


# Get all the directories in current path and child folders
def get_all_dirs(path='.'):
    files = []
    dirs = []

    for item in listdir(path):
        if path[-1] == sep:
            path = path[:-1]
        full_path = path + sep + item
        files.append(full_path)

    while files:
        elem = files.pop()

        if not isfile(elem):
            dirs.append(elem)
            more_dirs = listdir(elem)
            for e in more_dirs:
                full_path = elem + sep + e
                files.append(full_path)

    return dirs


def rename_all_files(path, src_ext, dst_ext):
    list_of_files = get_all_files(path, src_ext)
    renamed_files = []
    for f in list_of_files:
        split_f = f.rsplit('.', 1)
        joined_f = split_f[:-1]
        joined_f.append(dst_ext)
        joined_f = '.'.join(joined_f)
        rename(f, joined_f)
        renamed_files.append([f, joined_f])
    return renamed_files
