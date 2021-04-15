def prompt_open(permission):
    file_handle = input("Enter a filename")
    while True:
        try:
            file_handle = open(file_handle, permission)
            return file_handle
        except FileNotFoundError or NameError:
            if permission != 'r' or 'w':
                print("Input correct permission!")
                permission = input()
            else:
                file_handle = input("Re-Enter file name")


print("Enter r to read file or w to write file \n")
argument = input()
file = prompt_open(argument)
print(file)
