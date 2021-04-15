def func1(list1, list2, str1):
	if len(list1) > 3:       
		list1 = list1[:3]   
	list2[0] = 'goodbye'
	str1 = ''.join(list2)
	
	
arg1_list = ['a', 'b', 'c', 'd']
arg2_list = ['hello', 'mother', 'and', 'father']
arg_str = 'sister'


func1(arg1_list, arg2_list, arg_str)

print(arg1_list)  # Line 1
print(arg2_list)  # Line 2
print(arg_str)  # Line 3

# (a) What output is produced by Line 1 when the program is executed?  
# (b) What output is produced by Line 2 when the program is executed?
# (c) What output is produced by Line 3 when the program is executed?