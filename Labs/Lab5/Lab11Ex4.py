L = [1,2,3,4]
list1 = []
str2 = ''

for x in range(len(L)):
    list1 += str(L[x])
str2 = str2.join(list1)

print(str2)