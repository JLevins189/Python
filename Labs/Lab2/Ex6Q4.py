num1str = input("enter a number: ")
num1 = int(num1str)
factorial = 1
 
for i in range(1, num1 + 1):
	factorial = factorial * i
 
print("factorial of ", num1, " is ", factorial)