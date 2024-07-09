# def hello():
#     print("hello world")
# hello()
# def add():
#     x=34
#     y=56
#     print(x+y)
# add()

# def add(x,y):
#     print(x+y)
# add(12,45)
# add(12,34)
# def rect(length,width):
#     print("the area of the rectangle is",length*width)
# rect(12,20)

#return statement:
# def hello():
#     return("hello world")
# print(hello())

# def add(a,b):
#     return(a+b)
# print(add(12,4))
#Recursion in python
def hello():
    print("hello")
    return hello()

def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
print(fact(4))

#lambda function
a = lambda b : b*5
print(a(4))

x=lambda a,b,c:(a+b)*c
print(x(3,7,5))

#local variables
# x=24
# print("first variable x",x)
# def hello():
#     x=25 
#     return x
# print(hello())

#global variable
x=24
print("first variable x",x)
def hello():
    global x
    x=25 
    return x
print(hello())