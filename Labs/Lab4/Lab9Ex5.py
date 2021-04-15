def factorial(my_num):
	counter = 1
	answer = 1
    
	for counter in range(1, my_num+1):
		answer = answer*counter			
	print(answer)
    
number = int(input("Input a number"))    
factorial(number)    