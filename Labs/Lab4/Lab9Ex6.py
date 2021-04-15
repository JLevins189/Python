def stringop(my_str1):
    
    if len(my_str1) < 4:
        print("Not enough characters, 4 required!")
    else:    
        str = my_str1[0:2] + my_str1[-2:]
	
    print(str)				
            
    
my_str = input("Input a string")    
stringop(my_str)    