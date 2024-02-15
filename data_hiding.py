class Person:
    def __init__(self, name, age):
        self.__name = name   #(Double underscore for making a variable private)
        self.__age = age
        
person1=Person("Messi",35)
print(person1._Person__name)
    