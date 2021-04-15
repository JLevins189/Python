int1str=input("Enter the first number \n")
int2str=input("Enter the second number \n")
int3str=input("Enter the third number \n")

int1=int(int1str)
int2=int(int2str)
int3=int(int3str)

if (int1>int2 and int1>int3):
    print("The first number is the highest")
elif(int2>int1 and int2>int3):
    print("The second number is the highest")
elif(int3>int1 and int3>int2):
    print("The third number is the highest")
    
    