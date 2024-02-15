class A:  # A- Parent class
    def method1(self):
        print("This is method 1")
    def method2(self):
        print("This is method 2")
class B:  # B- Parent Class
    def method3(self):
        print("This is method 3")
    def method4(self):
        print("This is method 4")

# Multiple Inheritance (Multiple classes are inherited in a single class)
class C(A,B):   # In Multiple Inheritance Preference is given to Left class i.e.,A 
    def method7(self):
        print("This is method 5")
obj=C()
obj.method3()
obj.method7()