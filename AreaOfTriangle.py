side1=float(input("Enter first side of triangle:"))
side2=float(input("Enter second side of triangle:"))
side3=float(input("Enter third side of triangle:"))
s=(side1+side2+side3)/2
a=((s*(s-side1)*(s-side2)*(s-side3))**(1/2))
print("Area of triangle:",a)
