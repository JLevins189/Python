def even_num(nums1):
    even = []
    for j in range(0, len(nums1)):
        if nums1[j] % 2 == 0:
            even.append(nums1[j])
    print(even)
    

numbers = []
n = int(input("How many numbers would you like to enter \n"))
for i in range(0, n):
    temp = int(input("Enter a number"))
    numbers.append(temp)
even_num(numbers)    
