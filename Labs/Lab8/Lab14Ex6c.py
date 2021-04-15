def remove_even(list_num1):
	list_num2 = []
	for i in range(0, len(list_num1)):
		if list_num1[i] % 2 != 0:
			list_num2.append(list_num1[i])
			

	return list_num2


def remove_odd(list_num1):
	list_num2 = []
	for i in range(0, len(list_num1)):
		if list_num1[i] % 2 == 0:
			list_num2.append(list_num1[i])
			

	return list_num2
	
	
def remove_even_or_odd(Bool,list_num3):
    if Bool == True:
        list_num3 = remove_odd(list_num3)		
    elif Bool is False:
        list_num3 = remove_even(list_num3)	
        
    return list_num3    

	
list_num = [1,2,3,4,5,6,7,8,9,10]
Boolean = False
# Boolean = False
list_num = remove_even_or_odd(Boolean, list_num)
print(list_num)	

