int1 = 100
counter=0


while (int1 >= 100 and int1 < 1000):
    if (int1 % 17 == 0):
        int1+=1
        print(int1)
        counter+=1
    else:
        int1+=1




print("\n",counter, "3 digit numbers are divisable by 17")	