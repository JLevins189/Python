def count_o(str1, char1):
    count = 0
    list1 = str1.split()
    for i in range(0, len(list1)):
        if list1[i][0] == char1:
            count += 1
    print("Words beginning with", char1, count)
    

s = input("Enter a multiple word string \n")
character1 = input("Pick a letter to check the beginning of a word for\n")
count_o(s, character1)
