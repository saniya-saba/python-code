fruit = ["apply","mango","banana",]
fruits = ["appple","banana","mango",122,222,234]
print(fruit)
print(fruits)

#silicing lists
# a=["irinman","thor","captain america","hulk"]
# print(a[2])
# print(a[1:3])
# print(a[:3])
# print(a[1:])
# print(a[::-1])
# print(a[-1:-4:-1])
# print(a[-3:-1])


#list iteration
#iteration using for loop
a=["ironman","thor","captain america","hulk","black panther","vision"]
# for i in a:
#   print(i)

#iteration using using for loop range and length function
# for i in range (len(a)):
#   print(a[i])

#oteration using while loop
# i=0 
# while i < (len(a)):
#   print(a[i])
#   i+=1
# using short hand for loop
# [print(i) for i in a]

#1.to find the length of the list
print(len(a))

#2.to count an occurence of a particukar elemnt
print(a.count("vision"))

#3. to add the list
a.append('spiderman')
print(a)

#to add to a specific location
a.insert(1,"vision")
print(a)

#to remove from a list
a.remove("hulk")
print(a)

#to remove from certain location 
print(a.pop(4))

#to create a copy of a list
b=a.copy() 
print(b)

b=[a.copy()]
print(a)

#to access an element 
print(a.index("vision"))

#to entend the list
c=["vision","spiderman"]
a.extend(c)
print(a)

#to rever the list
a.reverse()
print(a)

#to sort the list
a.sort()
print(a)
d=[1,8,9,4,5,8,7,5,0]
d.sort()
print(d)

#to clear the data from the list
a.clear()
print(a)

d.clear()
print(d)

#list comparehension
l1 = [30,40,50,56,70,80,90]
l2=[ ]
for i in l1:
  if i>45:
    l2.append(i)
    print(l1,"\n",l2)
    l3 = [i for i in l1 if i > 45 ]
    print(l3)