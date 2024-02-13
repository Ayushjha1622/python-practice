# Program to find sum of all the  numbers before that number and the number itself.
def sum_recursion(num):
    if num==0:
        return 0
    return num+sum_recursion(num-1)
ans=sum_recursion(5)
print("Sum of all the number including  that number is:")
print(ans)