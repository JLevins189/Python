str_length=input("Input an integer")
int_length=int(str_length)
i=1
sum=0

while (i <= int_length):
	sum = sum + i
	i+=1
    
counter=i-1	
if(sum % counter == 0):
    print(sum)
else:
    print("Sum is not divisible by number of operands")
    
    
