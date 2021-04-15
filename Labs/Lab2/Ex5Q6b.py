temperature=input("Enter the temperature \n")
temperatureint = int(temperature)

summer=input("Is it the summer (y/n) \n")

if (summer == "y"):
    if if (temperatureint >= 60 and temperatureint <= 100):
        print("The squirells play")
    else:
        print("The squirells don't play")    
elif (summer == "n"):
    if (temperatureint >= 60 and temperatureint <= 90):
        print("The squirells play")
    else:
        print("The squirells don't play")
	
	