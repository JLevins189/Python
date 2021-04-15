import string

str = input("Input a string\n")
str = str.lower()

str = str.strip(string.whitespace)
str = str.strip(string.punctuation)


#reverse
reverse_str=[]
reverse_str = str[::-1]  


if (str == reverse_str):
    print("\nString is palindrome")
else:
    print("\nString is not palindrome")
    
   
