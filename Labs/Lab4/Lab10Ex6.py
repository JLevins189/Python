def list_100(list1):
    for i in range(0, 100):
        list1.append(i)
        

list0 = []
list_100(list0)
list_num = int(input("Enter the index you want to see value of \n"))
print(list0[list_num])        
