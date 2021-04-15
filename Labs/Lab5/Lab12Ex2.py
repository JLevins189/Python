def safe_input(prompt, type):
    input_var = ''
    while True:
        try:
            if type == 'int':
                input_var = input(prompt)
                int(input_var)
                return input_var
            elif type == 'string':
                input_var = input(prompt)
                return input_var
            elif type == 'float':
                input_var = input(prompt)
                float(input_var)
                return input_var
            else:
                print("Incorrect type entered! \n")
        except ValueError or TypeError:
            if input_var is not type1:
                print(type, "not detected! Input correct type")
                input_var = input()
            else:
                break


type1 = input("Enter the type of input you wish to display\n int float or string\n")
prompt1 = input("Enter the prompt to display")
output = safe_input(prompt1, type1)
print(output)
