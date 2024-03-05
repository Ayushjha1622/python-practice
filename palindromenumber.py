# Program to check whether given number is Palindrome or not
num=int(input("Enter a number: "))
p=num
r=0
while num>0:
    a=num%10
    num=num//10
    r=r*10+a
if p==r:
    print(p,"is a Palindrome Number")
else:
    print(p,"is not a Palindrome number")