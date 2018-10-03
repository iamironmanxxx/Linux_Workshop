a=[1,2,3,4]
print(a)
print(type(a))

print(a[:]) #prints all
print(a[2:]) #prints from 2 to rest
print(a[:5]) #from beginning to 5
print(a[-2]) # 2nd last element
print(id(a))
a.append(10) #insert from rear
print(a)
print(id(a))#id remains same because it is a mutable type
a.insert(3,100) #insert at 3rd index
print(a)
b=[2,3,4,2]
print(b)
b.remove(2) #removes first appearance of 2
print(b)

for x in z: #iterating a list
	print(x)
