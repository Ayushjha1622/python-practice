glovar=int(input("enter your number: "))

def test1():
    print(glovar)


def test2():
    global glovar
    glovar="good morning"
    print(glovar)
    
    
test1()
test2()