cigars=input("Enter the number of cigars \n")
cigarsint = int(cigars)

weekend=input("Is it the weekend (y/n) \n")

if (weekend == "y"):
    if (cigarsint>=40):
        print("This was a success")
    else:
        print("This wasn't a success")    
elif (weekend == "n"):
    if (cigarsint >= 40 and cigarsint <= 60):
        print("This was a success")
    else:
        print("This wasn't a success")
	
	