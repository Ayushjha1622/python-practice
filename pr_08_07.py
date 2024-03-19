def remove_and_strip(String,word):
    newstr=String.replace(word,"")
    return newstr.strip()


this = "      haary is good          "
n=remove_and_strip(this,"harry")
print(n)
