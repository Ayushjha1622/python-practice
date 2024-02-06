#object
a=5
isinstance(a,object) 
a+4
isinstance(a,int) 

def func(): 
    pass
isinstance(func,object) # ---> True

class A:
    name="jatin"
    marks=50

type(A) 
A=5
type(A) 

class A:
    def __call__(self):
        print("You called me")

a=A()
type(a) 
a() 

b=A.__call__()
b=A()

def func():
    print("Hello") 
func()
func.__call__() 

def say_hi(self):
    print(self.name)
    self.name="anonymous"

for i in range(5):
    print(i)
#Even for for loop there is dunders

a={"name":"Jatin"}

a.__getitem__("name")  

class Exponent:
    def __init__(self,n):
        self.n=n
    def __getitem__(self,x):
        return x**self.n
e=Exponent(3)
e[6] 

class A:
    name="Jatin"
    def __init__(self,n):
        self.n=n
a=A(2)
a.name 
a.n 


class Dog:
    kind='canine'
    def __init__(self,name):
        self.name=name
a=Dog("Maxx")
a.name 
a.kind 


class Dog:
    tricks=[]
    def __init__(self,name):
        self.name=name
    def add_tricks(self,trick):
        self.tricks.append(trick)
d1=Dog("Maxx")

d1.add_tricks("fetch")
d1.add_tricks("talk")
d1.tricks 
d2=Dog("Bella")
d2.tricks 

