#private members can be created by adding "__" (double "_") before var name
class temp:
	var1=0 # class variable
	
	#constructor
	def __init__(self,var2,var3):
		self.a=var2
		self.b= var3
		temp.var1=temp.var1+1
	
	def func(self,var2,var3):
		return var2*var3
	
	def func1(self):
		return self.a*self.b
	def fun2(self):
		print("Hello World")


obj=temp(3,4)
print(obj.a,obj.b,obj.var1)
print(obj.func(4,5))
print(obj.func1())
print(obj.fun2())
obj.c=8 #dynamically adding a member variable that are unique for that instance
print(obj.c)
