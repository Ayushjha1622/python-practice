x=int(input("Enter 1st variable:"))
y=int(input("Enter 2nd varaible:"))
a=bin(x)
b=oct(y)
print(a)
print(b)
print(a[2:],",",b[2:],sep="") #sep="" is used for removing space which is developed by default because of ,