f=open("temp.txt","w+") #the file needn't be created before running this 
f.write("This is line1\n")
f.write("This is line2\n")
f.write(str(1234)+"\n")#type-cast 1234 to string
f.close()

with open("temp.txt","r") as f:
	for line in f:
		print(line) #extra newlines coz of print and \n

f=open("temp.txt","r")
print(f.readlines())#read all lines and store them in an array and "increment line by 1"
print(f.readline())#to read a line and "increment line by 1"


