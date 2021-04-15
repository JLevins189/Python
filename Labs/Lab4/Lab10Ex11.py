def convert_int(list1):
	string1 = ""
	for i in range(0, len(list1)):
		string1 += str(list1[i])
	numbers = int(string1)
	print(numbers)


list0 = []
length = int(input("Enter how many elements in the list \n"))

for j in range(0, length):
	temp = int(input("Enter element \n"))
	list0.append(temp)

convert_int(list0)
