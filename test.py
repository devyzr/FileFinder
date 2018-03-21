import FileFinder


def print_all(x):
    print('-------')
    for y in x:
        print(y)
    print('-------')


x = FileFinder.get_files()
print("Get files")
print_all(x)

x = FileFinder.get_all_files()
print("Get all files:")
print_all(x)

x = FileFinder.get_all_files(extension='py')
print("Get all files (python extension):")
print_all(x)

x = FileFinder.get_dirs()
print("Get dirs:")
print_all(x)

x = FileFinder.get_all_dirs()
print("Get all dirs:")
print_all(x)


# This is a bad test, do not rely on it!
