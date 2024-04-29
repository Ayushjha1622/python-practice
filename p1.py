#Program to check whether first letter is vowel or not of given string
str=input("Enter a new string:")
a=str[0]
if a in ["a","e","i","o","u","A","E","I","O","U"]:
    print("Vowel")
else:
    print("Not a Vowel")