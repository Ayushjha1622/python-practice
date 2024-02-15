# POLYMORPHISM - Different(Many/Multiple) forms
# exp- len() function is an example of polymorphism which finds length of different data types 

print(len("Hello"))
print(len([12,23,434]))


def add(num1,num2,num3 = 0):  # default value of all three variables is 0.
    return num1 + num2 + num3
print(add(5,8))  
print(add(2,3,5))


class India:
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("Developing")
        
class USA:
    def capital(self):
        print("Washington DC")
    def language(self):
        print("English")
    def type(self):
        print("Developed")
        
obj1= India()
obj2= USA()

for i in (obj1,obj2):
    i.capital()
    i.language()
    i.type()

# Method overriding
    
class Bird: # Bird- Parent class
    def character(self):
        print("Bird has two wings and two legs")
    def eyes(self):
        print("Bird has two eyes")
    def fly(self):
        print("Most of the birds can fly")
class Sparrow(Bird):  # Sparrow- Child class
    def fly(self):
        print("Sparrow can fly")
class Ostrich(Bird): # Ostrich- child class
    def fly(self):
        print("Ostrich can't fly")
bird=Bird()
sparrow=Sparrow()
ostrich=Ostrich()

bird.eyes()
bird.character()
bird.fly()
sparrow.eyes()
sparrow.fly()
ostrich.fly()
    