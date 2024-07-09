#1.write a program to find max and min in a set
a={12,13,14,45,67,46,57,87}
maximum=max(a)
minimum=min(a)
print("maximum value:",maximum)
print("minimum value:",minimum)

#2.write a program to find comman elments in three list using sets
a=[1,2,3,4,5,6]
b=[2,3,4,5,7]
c=[8,9,5,4]
print(set(a)&set(b)&set(c))

#3.write a program to find differnce between two sets 
a={1,3,4,6,5,7}
b={4,5,6,8}
print(a.difference(b))
print(b.difference(a))
print(b.issubset(a))

#4.wtrite a program to remove an item from a set if it is present in the set
d={1,3,5,7}
d.discard(5)
print(d)


