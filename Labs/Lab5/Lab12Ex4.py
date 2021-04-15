def number_op(num1, num2, num3):
    while True:
        try:
            answer = (num2/num1) + num3
            return answer
        except ValueError or ZeroDivisionError:
            if num1 == 0:
                num1 = int(input("First number cannot be zero\nEnter another number"))
            elif num1 or num2 or num3 is not int:
                print("Error with number values\n")
                num1 = int(input("Enter another first number \n"))
                num2 = int(input("Enter another second number \n"))
                num3 = int(input("Enter another third number \n"))
            else:
                break


numbr1 = int(input("Enter first number \n"))
numbr2 = int(input("Enter second number \n"))
numbr3 = int(input("Enter third number \n"))
output = number_op(numbr1, numbr2, numbr3)
print('(', numbr2, '/', numbr1, ') + ', numbr3, '=', output)
