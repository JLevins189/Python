def insert_string_middle(my_str1,add_string):
    str = ""
    half = len(my_str1) // 2

    for counter in range(0,half):
        str += my_str1[counter]
    
    str+=add_string  
    
    for counter in range(half,len(my_str1)):
        str += my_str1[counter]

    print(str)
	
	
my_str1 = input("Input a string")    
add_string = input("Input a string to be added in the middle") 
insert_string_middle(my_str1,add_string)