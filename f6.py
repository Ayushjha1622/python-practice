# * is used for giving arguments without defining parameters
def details(name,*data):
    print(name)
    print(data)
details("Shivani Singh","Uttar Pradesh",18,8077000000)

# ** is used for key value pairs in parameters

def detail(**data):  # **data(any variable name) and generally it is args(arguments)
    print(data)
detail(Name="Shivani Singh",Place="Uttar Pradesh",Age=18)


# Program to know scpoe of varaibles 
a=10
def func():
    a=15
    print(a)
func()
print(a)

# Program to access Global Variables in function and modify it 

a=10
def func1():
    global a
    a=15
    print(a)
func1()
print(a)