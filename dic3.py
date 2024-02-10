# NESTED DICTIONARY
dic1={"class":{"student":{"name":"xyz","mark":{"python":95,"HTML":90}}}}
print(dic1["class"]["student"]["mark"]["python"])
print(dic1["class"]["student"]["mark"]["HTML"])
an=dic1.get("class",{}).get("student",{}).get("mark",{}).get("python")
print(an) 