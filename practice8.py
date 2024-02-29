# Take an integer n from the user. Your task is to multiply the pi value with itself for n times
# without using any arithmetic operator and print the result up to 3 decimal places.

import math
n=int(input("Enter a number: "))
res=math.pi
product=1
for a in range(0,n):
    product*=res
print(format(product,".3f"))