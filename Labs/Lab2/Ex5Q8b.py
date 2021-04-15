str_length=input("Input an integer")
int_length=int(str_length)
i=1
sum=0
sum_of_sums = 0

while (i <= int_length):
	sum = sum + i
	i+=1
	sum_of_sums = sum_of_sums + sum
print("The consecutive integers sums add up to ",sum_of_sums)	
	
