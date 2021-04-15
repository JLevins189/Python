answer=0
finish=0
int1str=input("Enter the first number \n")
int2str=input("Enter the second number \n")

int1=int(int1str)
int2=int(int2str)

while finish!=1:
    print("\nEnter a mathematical operation to perform	")
    operator=input(" + or - or x or / (divide)\n")

    if(operator=="+"):
        answer=int1+int2
        print(answer)
        finish=1
    elif(operator=="-"):
        answer=int1-int2
        print(answer)
        finish=1
    elif(operator=="x" or operator=="X"):
        answer=int1*int2
        print(answer)
        finish=1
    elif(operator=="/"):
        answer=int1/int2 
        print(answer)
        finish=1
    else:
        print("Invailid input detected... Try again \n")
        
