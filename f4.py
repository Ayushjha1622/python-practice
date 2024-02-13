#creat a function to print your name and age

def intro(name,age):
    return name,age          #Return elements in form of tuples
name=input("Enter your Name: ")
age=int(input("Enter Your Age:"))
print(intro(name,age))