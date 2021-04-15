my_dict = {'a':15 , 'c':35, 'b':20}

for key, value in my_dict.items():   
	print(key)  #a)

for key, value in my_dict.items():   
	print(value)  #b)

for key, value in my_dict.items():   
	print(key, value)  #c)      


sorted(data.values())
sorted(data.items(), key=lambda x:x[1])

   