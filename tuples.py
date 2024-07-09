# a="apple","mango","banana"
# print(type(a))
# print(a)
# b=("ironman",)
# print(type(b))

#silicing in tuples:
# a=("oneplus","redmi","vivo","sumsung","nokia")
# print(a[1:3])
# print(a[:3])
# print(a[2:3])
# print(a[::2])
# print(a[1::2])
# print(a[2::3])

#with for loop
# for i in a:
#   print(i)

#along with range and length in for loop 
# for i in range(len(a)):
#   print(a[i])  

#along with while loop
# i=0
# while i < len(a):
#   print(a[i])
#   i+=1

#conversion of tuples and tuple function
# a=("oneplus","nokia","redmi")
# print(a)
# print("before conversion:",type(a))
# a=list(a)
# print("ofter conversion:",type(a))
# a.append("vivo")
# print(a)
# a=tuple(a)
# print(type(a))
# print(a)
# #count method 
# print(a.count("redmi"))
# #index
# print("that the index of nokia is",a.index("redmi"))

#1.convert the following dectionary into JSON format 
# import json
student_data={"name":"david", "age":13 , "marks":87}
# print(type(student_data))
# data=json.dumps(student_data)
# print(type(data))
student_data = json.loads(student_data)
print(student_data)
data = json.loads(student_data)
print(data["age"])

#3.acess the nested key "marks"from the following nested data
import json
student_data="""{"student":
{"grade":
{"name":"david",
"marks":87}
}
}"""
data=json.loads(student_data)
print(data["student"]["grade"]["marks"])


