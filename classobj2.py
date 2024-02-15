class Car:
    wheels=4
    # Static variable: Value does not change and is accessible by whole class.
    # Instance variables: value varies from object to object
    def __init__(self):
        self.company="BMW"
        self.mileage=10
car1=Car()
car2=Car()
print(Car.wheels)
print(car1.company,car1.wheels)
print(car2.company,car2.wheels)
Car.wheels=5
print(Car.wheels)