f=open("img.png","rb")
f1=open("img3.png","wb")
for i in f:
    f1.write(i)

f2=open("img3.png","rb")
print(f2.read())