tup=("Red","Yellow","Green")
print(tup)
# Appending element by type casting tuple to list
l=list(tup)
l.append("white")
print(l)
# Modified tuple
tup=tuple(l)
print(tup)

# Add two tuples
tuple1=(1,2,3,4)
tuple2=(5,6,7,8)
tupl=tuple1+tuple2
print(tupl)


# Reverse tuple
tuple1=(1,2,3,4,5)
new_tuple=tuple1[::-1]
print(new_tuple)

# tuple of your Name 
tup1=["shivani"]
print(tuple(tup1))
# Tuple of each letter present in your name.
name=("shivani")
print(tuple(name))