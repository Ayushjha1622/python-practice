# myDict = {                                      #mutable
#     "fast": "in a quick manner",                #unordered
#     "harry": "a coder",                         #cannot contain duplicate keys
#     "marks": [1,2,5],                           #indexed
#     "anotherdict":{'harry':'player'}
#     }

# # print(myDict.keys())
# # print(list(myDict.keys()))        #prints the keys of dictionary                             #prints the keys of dictionary
# # print(myDict.values())            #prints the keys of dictionary  
# # print(myDict.items())             #prints the (key,value) for all contents of the dictionary
# # print(type(myDict.keys()))
# updateDict = {
#     "lovish": "friend",
#     "divya": "friend",
#     "harry": "A dancer",

# }
# myDict.update(updateDict)  #updates the dict by adding key-value pairs from updateDict
# print(myDict)
# print(myDict.get("harry"))
# print(myDict.get("harry"))


ep1 = {122: 45, 123:89, 567:69, 670:69}
ep2 = {222:67, 566:90}

# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
# ep1.popitem()   #deletes last item

del ep1[122]

print(ep1)
