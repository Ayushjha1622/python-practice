# INHERITANCE - use classes in different classes to avoid repetition

class A:  # A- Parent class
    def __init__(self):
        print("Init of Class A")
    def method1(self):
        print("This is method 1")
    def method2(self):
        print("This is method 2")
class B(A):  # B- Child class
    def __init__(self):
        super().__init__()
        print("Init of Class B")
    def method3(self):
        print("This is method 3")
    def method4(self):
        print("This is method 4")
class C(B): # C- Child class
    def __init__(self):
        super().__init__()
        print("Init of Class C")    # First class will check if it has __init__ or not if it has then it will run only it's __init__ .
    def method5(self):
        print("This is method 5")
    def method6(self):
        print("This is method 6")
obj=C()
obj.method1()
obj.method3()
obj.method6()


    