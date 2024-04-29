# str=input("str: ")
# result=""
# for i in range(len(str)):
#     x=str[0:i+1]
#     result=result+x
# print(result)


# x=input("str: ")
# for i in x.split("-"):
#     print(i,end="")


# armstrong number 
# n=int(input("num: "))
# sum=0
# temp=n

# while temp>0:
#     digit=temp%10
#     sum+=digit**3
#     temp//=10
    
# if(n==sum):
#     print(n,"armstrong")
# else:
#     print("not armstrong")


# n=int(input("num: "))
# sum=0
# temp=n
# while temp>0:
#     digit=temp%10
#     sum+=digit**3
#     temp//=10
# if n==sum:
#     print(n,"armstrong")
# else:
#     print(n,"is not armstrong")



# prime number
# num=29
# flag=False

# if num==1:
#     print(num,"is not prime")
# elif num>1:
#     for i in range(2,num):
#         if(num%i) ==0:
#             flag = True
#             break
#     if flag:
#         print("not prime")
#     else:
#         print("is prime")



# palindrome
# def palindrome(s):
#     s=''.join(char.lower() for char in s if char.isalnum())
#     return s == s[::-1]

# string=input("string: ")
# if palindrome(string):
#     print("yes".format(string))
# else:
#     print("no".format(string))



# fibonacci

def fibonacci(n):
    sequence=[0,1]
    while len(sequence) <n:
        next_term=sequence[-1]+sequence[-2]
        sequence.append(next_term)
    return sequence

num=int(input("enter your number: "))
fib_seq=fibonacci(num)
print("seq".format(num))
print(fib_seq)
    