mydic={"Name":"Shivani","Age":18,"Percent":96.2}
print(mydic)
#if we try to add duplicate value then previous value updates/overwrite by new value bcz dictionary doesn't allow duplicates.
print(mydic.get("Age"))
print(mydic.keys())
print(mydic.values())
print(mydic.items())
mydic["Roll no."]=65
print(mydic)
# mydic["Roll no."]=54
mydic.update({"Roll no.":54})
print(mydic)
mydic.pop("Age") # we have to give key and that key-value pair will be deleted
mydic.popitem()  # removes last key-value pair
print(mydic)
del mydic  #deletes th dictionary
