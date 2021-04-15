def remove_substring(my_str1, indice1, indice2):
    str = ""
    my_str1.replace(" ", "")

    for counter in range(0,indice1):
        str += my_str1[counter]

    for counter in range(indice2+1,len(my_str1)):
        str += my_str1[counter]

    print(str)
	
	
my_str1 = input("Input a string")    
indice1 = int(input("Input a element number range start to be removed from")) 
indice2 = int(input("Input a element number range end to be removed from")) 
remove_substring(my_str1, indice1, indice2)

