myDict = {"pankha": "fan", "vastu":"item", "dabba":"container"}

print("options are: ",myDict.keys())
a=input("enter the hindi word: ")
# print("the meaning of your word is: ",myDict[a])  
print("the meaning of your word is: ",myDict.get(a))
