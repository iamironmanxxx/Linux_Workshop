#!/usr/bin/python3
a=5
b=2.3
c="xyz"
d=(1,2,3) #tuple type 
print (a,b,c)
print (d)
print(id(a)) #address of a
z=a
print(id(z)) #has same address as that of a because in python all are reference types and are passed by reference
f=5
print(id(f)) #same address because in python strings,ints,doubles constants have same ref
a=5
print(id(a)) # a new mem block is created and so address changes
print(type(a)) #prints type of a
print(type(b)) #prints type of b
print(type(d)) #prints type of d
print(type(f)) #prints type of f
str="123"
e=int(str); #converts to int
print(type(e))
str="123.45"
g=float(str)
print(type(g))
