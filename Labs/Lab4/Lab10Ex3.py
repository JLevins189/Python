def count_o(str1):
    count=0
    list = str1.split()
    for i in range(0,len(list)):
        if(list[i][0] =='o'):
            count+=1
    print("Words beginnning with o", count)
    
str = input("Enter a multiple word string \n")
count_o(str)
    
    