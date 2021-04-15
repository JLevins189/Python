#Question 12
#Input
my_weight_imperial = input("Enter your weight in pounds")
my_weight_imperial = float(my_weight_imperial)

my_height_imperial = input("Enter your height in inches")
my_height_imperial = float(my_height_imperial)


#Conversion
my_weight = my_weight_imperial * 0.453592
my_height = my_height_imperial * 0.0254

#Print
print("Your BMI is", my_weight / my_height**2)