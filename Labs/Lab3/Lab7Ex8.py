str = input("Input a string")
new_str = ''
		
for c in str:
	new_str += chr(ord(c) + 1)
    
print(new_str)    