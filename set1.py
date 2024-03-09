set={"car","bike","boat","cycle","train"}
# print(set)
# for a in set:
#     if a=="bike":
#         print("True")
#     else:
#         print("False")
# # or 
if "bike" in set:
    print("True")
else:
    print("False")
    
myset1={1,2,3,4}
myset2={4,5,6}
myset3=myset1.union(myset2)
myset4=myset1.intersection(myset2)
myset5=myset1.symmetric_difference(myset2)
print("Union of both sets is:",myset3)
print("Intersection of both sets is:",myset4)
print("Symmetric difference of both sets is:",myset5)

