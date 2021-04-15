def remove_duplicates(list1):
    list2 = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            list2.append(list1[i])
    return list2    


list0 = []           
length = int(input("Enter how many elements in the list \n"))
for j in range(0, length):
    temp = int(input("Enter element \n"))
    list0.append(temp)
    
new_list = remove_duplicates(list0)
print(new_list)    
