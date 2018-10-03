a=input().split(" ")# splits acc to delimiter provided; converts a to list

print(a)

b="abab=-cd-ef-gh-ij".split("-")
print(b)

print("&".join(a)) # joins with delimiter provided

str="abcdefg"
print(str)
# to change value at ith position
str=str[:2]+"f"+str[3:]
print(str)

#for iterations possible with a single statement; list comprehension

# making a list of int type
a=[int(x) for x in input().split(" ")]
print (a)

#alternatively
a=[int(x) for x in ['12','3','4']]
print(a)
