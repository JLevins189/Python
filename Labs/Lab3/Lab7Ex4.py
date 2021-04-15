str = input("Enter a string\n")
newstr = str[-2:]

if (len(str) > 3):
    print(str[0:2])
    print (newstr)
else :
    print("More characters required")