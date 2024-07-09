# employee_data = {"name":"john","age":"23","gender":"femal"}
# print(employee_data)
# print(employee_data["age"])

# #iteration in dictionary
# student={"name":"saniya","class":"10th","rollno":"23"}
# for x in student:
#   print(x)

# for y in student:
#   print(student[y])  

# for z in student.values():
#   print(z)

# for x,y in student.items():
#   print(x,"-",y)


#dictinary function 
# student={"name":"saniya","class":"10th","roll_no":"23"}
# #.get
# x=student.get("name")
# print(x)
# #.item
# a=student.items()
# print(a)
# #.keys
# b=student.keys()
# print(b)
# #values
# c=student.values()
# print(c)
# #copy 
# d=student.copy()
# print(d)
# #setdefault
# p=student.setdefault("roll_no",24)
# print(p)
# #nested dictionaries
# employees ={"""1:{"name":"saniya","age":21,"gender":"feamle"}
#             2:{"name":"saba","age":20,"gender":"femal"}
#             3:{"name":"asad","age":24,"gender":"male"}"""}
# print(employees)
# print(employees([1]["age"]))


#problem solving
#1.write a python program to sort a dictionary by value
a={"a":12,"b":23,"c":6,"d":91,"e":4}
print(sorted(a.values()))


#2.write a python program script to print a dictionary where the keys are number between 1 and 15 and the value are square of keys
a={ }
for i in range(1,16):
    a[i]=i**2
print(a)

#3.write a program to multiply all the items in a dictionary 
c={"a":12,"b":23,"c":6,"d":91,"e":4}
product = 1
for i in c:
    product *=c[i]
print(product)    

#to dictionary by keys 
c=sorted(c.keys())
print(c)