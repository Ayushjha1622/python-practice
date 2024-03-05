a=int(input("Enter a  three digit number:"))
temp=a
b=0
while (a>0):
    r=a%10  #Remainder
    print(r)
    b=(b*10)+r
    a=a//10  #Quotient
print("Reverse number is:",b)
print(int(temp/2)) #Divide 3 digit number by 2 and print the result in integer form
