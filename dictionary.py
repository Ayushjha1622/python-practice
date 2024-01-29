myDict = {                                    #mutable
    "fast": "in a quick manner",                #unordered
    "harry": "a coder",                         #cannot contain duplicate keys
    "marks": [1,2,5],                           #indexed
    "anotherdict":{'harry':'player'}
    }

print(myDict['fast'])
print(myDict['harry'])
myDict['marks']=[45,78]
print(myDict['marks'])
print(myDict['anotherdict']['harry'])