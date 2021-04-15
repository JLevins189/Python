def sumnum(my_num):
	counter=0
	sum=0
    
	for counter in range(0, my_num+1):
		sum = sum + counter
	print(sum)				
            
    
number = int(input("Input a number"))    
sumnum(number)    