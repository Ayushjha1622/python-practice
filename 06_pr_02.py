sub1 = int(input("enter first subject marks: "))
sub2 = int(input("enter second subject marks: "))
sub3 = int(input("enter third subject marks: "))

if(sub1 <33 or sub2<33 or sub3<33):
    print ("u r fail because u have less than 33% in one of the subjects")

elif(sub1+sub2+sub3)/3 <40:
    print("u r fail due to total percentage less than 40")
else:
    print("u r passed")