class student:
    collegeName="LPU"
    def __init__(self,python,web,maths,n):
        self.Subject1 = python   # Subject1 is Variable
        self.Subject2 = web
        self.Subject3 = maths
        self.numOfSub = n
    def average(self):
        avg=(self.Subject1+self.Subject2+self.Subject3)/3
        return avg   
    #Below is Class Method    
    # Class method doesn't take self as parameter they take [cls] as parameter
    @classmethod
    def collegeDetail(cls):
        return cls.collegeName
    
    # Static Method
    @staticmethod
    def staticMethod():
        print("This is a static method")
student1=student(5,6,7,3)
student2=student(8,9,6,3)
print(student1.average())
print(student2.average())
print(student.collegeDetail())
print(student.staticMethod())