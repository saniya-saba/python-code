# a={"ironman","hulk","thor","captain america"}
# print(a)
# print(type(a))
# for x in a:
#     print(x)

# a.add("spiderman")  
# print(a)  

# a.pop()
# print(a)

# a.remove("thor")
# print(a)

# a.discard("hulk")
# print(a)

# b=a.copy()
# print(b)

a={"ironman","hulk","thor","captain america"}
b={"superman","batman","wonder-woman"}
c={"hulk","thor","spiderman"}
#isdisjoint
print(a.isdisjoint(b))
print(a.isdisjoint(c))
#issubset
print(a.issubset(a))
print(a.issubset(b))
#issuperset
print(b.issuperset(b))
print(c.issuperset(c))
#update
x=a.update(a)
print(x)
#clear
print(a.clear())
#union
print(a.union(c))
#difference
a.difference(c)
print(c)
#difference_update
a.difference_update(c)
print(c)
#intersection
a.intersection(c)
print(c)
#intersection update
a.intersection_update(c)
print(c)
#symmetric difference
y=a.symmetric_difference(c)
print(y)
#symmersection difference_update
x=a.symmetric_difference_update(c)
print(y)
