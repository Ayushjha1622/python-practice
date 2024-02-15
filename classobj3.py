class student:
    def __init__(self,python,web,maths,n):
        self.Subject1 = python   # Subject1 is Variable
        self.Subject2 = web
        self.Subject3 = maths
        self.numOfSub = n
    def average(self):   # Instance method
        avg=(self.Subject1+self.Subject2+self.Subject3)/3
        return avg
    def get_subject1(self):
        return self.Subject1   # Accessor Method
    def set_marks(self,value):
        self.Subject1 = value   # Mutator Method
    
student1=student(4,7,8,3)
# Instance of the object is where object is inside memory
student2=student(7,8,9,3)
print(student1.average())
print(student2.average())


# geter type(Accessor type) = return value only 
# Mutator type =change/modify value only