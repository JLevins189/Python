def stringop(my_str1):
    str = ""
    half = len(my_str1) // 2
    for counter in range(0,half):
            str += my_str1[counter]
    print(str)


my_str1 = input("Input a string")    
stringop(my_str1)
