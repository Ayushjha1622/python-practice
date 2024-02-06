time=float(input("Enter Your Years of Services: "))
if time>5:
    salary=float(input("Enter your salary:"))
    bonus=salary+1000
    print("Net Bonus Amount is:",bonus)
else:
    print("sorry, No Bonus Because Your Year of Service is Less than 5 Years")
    