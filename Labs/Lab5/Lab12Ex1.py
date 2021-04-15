number_float = 0
while True:
    try:
        number_str = input("Input a floating-point number: ")
        number_float = float(number_str)
    except ValueError or TypeError:
        if number_float is not float:
            number_str = input("Error float not detected! Input a floating-point number: ")
        else:
            break
    print("Number is", number_float)

