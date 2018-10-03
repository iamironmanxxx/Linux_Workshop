#functions
#support multiple return values
def func():
	a = []
	for x in range(2,4) : 
		print (x)
		a.append(x)
	return a,"True"

#calling the function
print(func()) #prints both values returned

#yield - continuously returns value (object) without terminating the function 
def func2():
	a = []
	for x in range(18,22) :
		yield x
		a.append(x)
		return a
print([x for x in func2()])


def func3():
	a = []
	for x in range(18,22) :
		yield x
		a.append(x)
	a.append(99)	
	return a
print([x for x in func3()])
a=func3()
print(a)

#for multi params
def func4(*vars):
	for var in vars:
		print(var)
func4(2,3,4)

#for key, value pairs
def func5(**vars):
	for k,v in vars.items():
		print(k,v)

func5()
