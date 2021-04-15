decimal_str = input("Enter an integer")
decimal = int(decimal_str)
remainder = 0
count = 0
binary = []

if decimal > 256:
    print("Only numbers less than 256")
elif decimal == 0:
    print("0")
elif decimal < 0:
    print("Only positive numbers can be used")
else:
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary.append(remainder)

print(binary[::-1]) #Must print in reverse order to work
