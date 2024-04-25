def sum(list):
    if not list:
        return 0
    else:
        return list[0] + sum(list[1:])

l1=[1,2,3,4,5]
print(sum(l1))