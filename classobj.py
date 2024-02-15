class Laptop:
    # (pass) is for empty class
    def __init__(self): # whatever is written inside it wiil be returned without calling it.It is automatically called with object called.
        print("Hello world")
    def config(self):
        print("MSI","Lenevo","HP","Dell")
laptop1=Laptop()  # Object
laptop2=Laptop()
laptop1.config()  # OR
Laptop.config(laptop1)
laptop2.config()

class Student:
    def __init__(self,name,rollNo):
        self.name=name
        self.rollno=rollNo
# declare variables and stuff. no need to call this function it is automatically called by interpreter.
# Attributes-variables
# Behaivour - methods
    def info(self):
        print("Name is: ",self.name)
        print("RollNo. is: ",self.rollno)
object1=Student("Shivani","65")
object1.info()
print(id(object1))  # Memory Address {objects created in (HEAP Memory)}
object2=Student("Upasana","47")
object2.info()
print(id(object2))    # Memory Address
        
 
class Person():
    def __init__(self,name,number):
        self.name=name
        self.number=number #Jersey number
    def compare(self,other):
        # if (self.number==other.number):
        if (self.name==other.name):
            return True
        else:
            return False
        
object1=Person("Ishan","32")
object2=Person("Ishan","46")
print(object1.name)
print(object1.number)
print(object2.name)
print(object2.number)

print(object1.compare(object2))
               