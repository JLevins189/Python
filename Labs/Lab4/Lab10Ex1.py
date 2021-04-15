def add_num(numbers1):
    total = 0
    for ele1 in range(0, len(numbers1)):
        total = total + numbers1[ele1]
    print("Sum of numbers is\n", total)

numbers = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("Enter"))
    numbers.append(ele)
add_num(numbers)
