def stringop(my_str1):
    str = ""
    index = 0
    counter = 0
    str= ""
    for counter in range(len(my_str1)):
        if counter % 2 == 0:
            str += my_str1[counter]
    print(str)

my_str1 = input("Input a string")    
stringop(my_str1)
