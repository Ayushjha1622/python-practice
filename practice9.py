def And(x,y):
    return x&y
def Or(x,y):
    return x|y
def xor(x,y):
    return x^y
x=int(input("Enter value of integer: "))
y=int(input("Enter value of integer: "))
print(And(x,y))
print(Or(x,y))
print(xor(x,y))