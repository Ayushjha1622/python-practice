class A:
    def __init__(self,x):
        self.x=x
class B(A):
    def __init__(self,x,y):
        print("B init executed")

abc=B()


class A:
    def __init__(self):
        print("A init executed")
class B(A):
    def __init__(self,x,y):
        print("B init executed")



class A:
    def __init__(self):
        print("A init executed")
class B(A):
    def __init__(self,x,y):
        print("B init executed")
        super().__init__()
abc=B()

class A:
    pass
class B(A): 
    pass
class C(B):
    x=5
class D(A):
    x=10
class E(C,D): 
    pass
e=E()
print(e.x) 

class A:
    x=5
class B(A): 
    pass
class C(B):
    x=5
class D(A):
    x=10
class E(C,D): 
    pass
e=E()
print(e.x) 






a=range(5)
it=a.__iter__()
it.__next__() 
it.__next__() 
it.__next__() 
it.__next__() 
it.__next__() 


class myrange:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return myrange_iterator(self)
class myrange_iterator:
    def __init__(self,myrange):
        self.myrange=myrange
        self.i=0
    def __next__(self):
        ret=self.i
        self.i+=1
        if ret>=self.myrange.n:
            raise StopIteration
        return ret

a=myrange(5)
it=iter(a)
next(it)