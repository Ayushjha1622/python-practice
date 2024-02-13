#It should accept employer name and saalry and display both if the salary is missing then assign the default value 
# as 10000 to salary

def Job(name,salary=10000):
    print(name)
    print(salary)
name=input("Enter Your Name: ")
salary=int(input("Enter Your salary: "))
Job(name,salary)
Job("Ben")
Job("Mike",15000)