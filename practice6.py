a=["ross","rachel","manico","joe"]
#write a program to swap first and forth element 
# a[0],a[3]=a[3],a[0]
# print(a)

#write a program to add a new value at second position 
# a.insert(4,"phoebe")
# print(a)


#write a program to delet a value from 3rd position
a.pop(2)
print(a)


b=[13,14,12,45,15]
#write a program to multiply all the numbers in alist
mul=1
for i in (b):
  mul *= i
  print(mul)

# write a program to get the largest number from the list
b.sort()
print(b)
print("the largest value in the given list is",b[-1])
print("the smallest value in the give list is",b[0])
