def common_member(list1, list3):
    true = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            true = 1
    return true  


list0 = []  
list2 = []         
length = int(input("Enter how many elements in the lists \n"))

print("List1\n")
for j in range(0, length):
    temp = int(input("Enter element \n"))
    list0.append(temp)


print("List2\n")
for k in range(0, length):
    temp = int(input("Enter element \n"))
    list2.append(temp)    
    
boolean = common_member(list0, list2)
if boolean == 1:
    print("Common member detected \n")
else:
    print("Common member not detected \n")
 
