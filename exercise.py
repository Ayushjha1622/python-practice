# Create a class without any variables and methods
class A:  # A- Parent class
    pass

# Create a child class Bus that will inherit all the variables and methods of vehicle class

class vehicle:
    def __init__(self,name,milage):
        self.name=name
        self.milage=milage
class Bus(vehicle):
    pass
obj=Bus("SUV",40)
print(obj.name)
print(obj.milage)