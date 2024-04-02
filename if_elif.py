# ch=input("ch: ")
# if(ch>="a" and ch<="z") or (ch>="A" and ch<="Z"):
#     print("alphabet")
# elif(ch>="0" and ch<="9999999999"):
#     print("digit: ")
# else:
#     print("neither alpha nor ch")

# leap year
# year=int(input("year: "))
# if (year%4==0):
#     if(year%100==0):
#         if(year%400==0):
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")





# sumN
num=int(input("num: "))
i=0
sum=0
while(i<=num):
    if(i%2==0):
        sum+=i
    i+=1
print(sum)    