def iterate(my_num):
	counter=0
	
	for counter in range(0, my_num+1):
		if counter % 2 == 0:
			print(counter, "is even")
		else:	
			print(counter, "is odd")
            
    
number = int(input("Input a number"))    
iterate(number)    