# Program to replace those elements which are greater than 10 by 10.
lst=eval(input("Enter a list containing numbers:"))
length=len(lst)
for i in range(0,length):
    if lst[i]>10:
        lst.pop(i)
        lst.insert(i,10)
print(lst)