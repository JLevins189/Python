def minus_list(list1, list3):
    list4 = []
    for i in range(0, len(list1)-1):
        if list1[i] not in list2:
            list4.append(list1[i])
    return list4 


list0 = []  
list2 = []         
length = int(input("Enter how many elements in the lists \n"))

print("List1\n")
for j in range(0, length):
    temp = int(input("Enter element \n"))
    list0.append(temp)


print("\nList2\n")
for k in range(0, length):
    temp = int(input("Enter element \n"))
    list2.append(temp)    
    
list3 = minus_list(list0, list2)    
print("List 1 - List 2 is \n", list3)    
    

