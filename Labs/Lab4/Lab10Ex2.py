def max_list(list1):
	maximum = list1[0]
	for x in range(0, len(list1)):
		if maximum < list1[x]:
			maximum = list1[x]

	print("Max is", maximum)


numbers = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	ele = int(input("Enter"))
	numbers.append(ele)
max_list(numbers)
