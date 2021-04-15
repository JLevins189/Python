str = input("Enter a word")
x = len(str)
vowels = "aeiou"

#a)
if vowels in str[0]:
	str1[x] = 'y'
	str1[x+1] = 'a'
	str1[x+2] = 'y'
else: 
    str = str[1:] + str[0] + "ay"
    
print("In Pig latin that is", str)    