num = int(input("enter your number: "))
for i in range(10,0,-1):
    print(str(num) + "X" + str(i) + "=" + str(i*num))
    # print(f"{num}X{i}={num*i}")