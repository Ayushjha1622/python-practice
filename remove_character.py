str=input("str: ")
num=int(input("enter your number: "))
if num>len(str):
    print("invalid")
else:
    print("output: ",str[:num]+str[num+1:])