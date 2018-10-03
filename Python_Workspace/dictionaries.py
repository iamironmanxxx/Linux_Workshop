#sets and dictionaries can't be indexed
br=(1,2,3)
pqr = (1,2,3)
print(id(br))
print(id(pqr))
d={"abc" : 123 , 123 : "def" , "def" : 123 , br : [5,4,6]}
print(d)
print(d["abc"])

# deleting an entry

del d["abc"]

#adding a new key

d["shubh"]=364


#iterating a dictionary

for k,v in d.items() :
	print(k,v)

#taking input from user

#d={}
lis=(1,2,3)
xyz = (1,2,3)
print(id(br))
print(id(lis))
print(id(xyz))
print(id(pqr))
print (d[lis])

for i in range(4) :
	k,v=input("Enter key"),input("Enter value")
	d[k]=v
