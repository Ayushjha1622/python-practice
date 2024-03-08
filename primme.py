#Program to check whether given number is prime number or not
num=int(input("Enter a number greater than 1 or 2: "))
temp=num-1
p=0
while temp>1:
    if num%temp==0:
        p=1
        break
    temp-=1
if p==1:
    print(num,"is not a Prime number")
else:
    print(num,"is Prime number")