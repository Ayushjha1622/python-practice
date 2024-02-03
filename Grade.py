marks=float(input("Enter marks obtained by you:"))
total_marks=int(input("Enter total marks:"))
percent=(marks/total_marks)*100
if percent>=90:
    print("Grade A")
elif percent>=80 and percent<90:
    print("Grade B")
elif percent>=70 and percent<80:
    print("Grade C")
elif percent>=60 and percent<70:
    print("Grade D")
elif percent>=50 and percent<60:
    print("Grade E")
elif percent<50:
    print("Grade F")
else:
    print("Invalid input")
