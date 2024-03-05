str=input("Enter a string: ")
length=len(str)
b=0
for a in range(-1,(-length-1),-1):
    if str[b]==str[a]:
        c="y"
    else:
        c="n"
        break
    b+=1
if c=="y":
    print("String is Palindrome")
else:
    print("String is not Palindrome")