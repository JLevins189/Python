str = input("Input a string to be reversed\n")
reverse_str=[]


for i in range(1, len(str) + 1):
        reverse_str += str[len(str) - i]

print(reverse_str)	