class MyClass (object):
	def method1(self, param_list):
		self.local_list = []
		for element in param_list:
			if element > 10:
				self.local_list.append(element)
				
	def method2(self):
		self.sum_int = 0
		for element in self.local_list:
			self.sum_int += element
		return self.sum_int
		
		
		
inst1 = MyClass()
inst2 = MyClass()
inst1.method1([1,2,3])
print(inst1.local_list) # Line 1
inst1.method1([10,11,12])
print(inst1.local_list) # Line 2
print(inst1.method2()) # Line 3
#inst2.method2()		