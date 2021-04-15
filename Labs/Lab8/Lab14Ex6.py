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
	
	
list_num = [1,2,3,4,5,6,7,8,9,10]

menu = input("Enter e to remove even and o to remove odd numbers")
if menu == 'o':
	list_num = remove_odd(list_num)	
	print(list_num)		
elif menu == 'e':
	list_num = remove_even(list_num)	
	print(list_num)	
else:
	print("Error in input")
	print("Exit program!")