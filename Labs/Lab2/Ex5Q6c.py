speed=input("Enter the speed \n")
speedint = int(speed)

birthday=input("Is it the birthday (y/n) \n")

if (birthday == "y"):
    if (speedint < 65):
		print("No ticket")
	elif (speedint >= 66 and speedint <= 85):
        print("Small ticket")	
	elif (speedint >= 86):
		print("Big ticket")
elif (birthday == "n"):
    if (speedint < 60):
		print("No ticket")
	elif (speedint >= 61 and speedint <= 80):
        print("Small ticket")	
	elif (speedint >= 81):
		print("Big ticket")
	
	