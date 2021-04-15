import random

str = input("Input a string\n")
max = 0
length = len(str) - 1
i = random.randint(0,length)
j = random.randint(0,length)


while i==j: #keep generating
    i = random.randint(0,length)
    j = random.randint(0,length)


new_str = str[:i] + str[j] + str[i+1:j] + str[i] + str[j+1:]
print("Result", new_str)





