angle=float(input("Enter angle of Triangle: "))
if angle>180:
    print("Invalid Input")
else:
    if angle==90:
        print("Right angle")
    elif angle>90 and angle<180:
        print("Obtuse angle")
    elif angle<90:
        print("Actue angle")