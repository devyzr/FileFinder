import FileFinder


def print_all(x):
    print('-------')
    for y in x:
        print(y)
    print('-------')


x = FileFinder.get_all_files()
print_all(x)

x = FileFinder.get_all_files(extension='py')
print_all(x)

x = FileFinder.get_dirs()
print_all(x)

x = FileFinder.get_all_dirs()
print_all(x)


# This is a bad test, do not rely on it!
