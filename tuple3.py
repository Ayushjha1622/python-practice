#  For loop

myTuple=("Car","Bus","Truck")
for a in myTuple:
    print(a)
    
# While Loop
i=0
while i < len(myTuple):
    print(myTuple[i])
    i+=1
    
# Accessing element of List inside Tuple
tuple1=(1,2,[6,7],9,8,6,4)
print(tuple1)
print(tuple1[2][0])
tuple1[2].pop(0)
tuple1[2].insert(0,8)
print(tuple1[2][0])
print(tuple1)

# Or(x,y)
tuple1=(1,2,[6,7],9,8,6,4)
tuple1[2][0]=8
print(tuple1)