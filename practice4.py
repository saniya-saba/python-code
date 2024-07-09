#fibonacci series
# a=0
# b=1
# n=int(input("enter a number here:"))
# if n==1:
#   print(n)
# else:
#   print(a)
#   print(b)
# for i in range(2,n):
#   c=a+b
#   a=b
#   b=a
#   print(c)                  

#check a number is prime is or not
# num = int(input("enter a number here:"))
# if num <=1:
#   print("it is not a prime number")
# else:
#   for i in range(2,num):
#     if num%i==0:
#       print("number is not a prime number")
#       break
#     else:
#       print("it is a prime number")
#   print()
# print()

#check palindrome number 
# num = int (input("enter a number here:"))
# temp = num
# rev = 0
# while num>0:
#   dig = num%10
#   rev = num//10
#   num = num//10
#   if rev == temp:
#     print("it is palindrome")
#   else:
#     print("it is not a palindrome")
 
# area calculator
print("*******AREA CALCULATOR*********")
print(""" press 1 to get the area of squre
      press 2 to get the area of rectangle
      press 3 to get the area of circle 
      press 4 to get the area of triangle""")
choice = int(input("enter a number between 1-4:"))
if choice == 1:
  side = float(input("enter the length of one side:"))
  area = side**2
  print("the area of squre is", area)
elif choice == 2:
  length = float(input("enter the length of the rectangle:"))
  width = float(input("enter the width of the rectangle:"))
  area = length*width
  print("the area of rectangle is", area)
elif choice == 3:
  radius = float(input("enter the radiou of circle is:"))
  area = ((22/7)*(radius))
print ("the area of the circle is", area)
if choice == 4:
  base = float(input("enter the base of the triangle:"))
  height = float(input("enter the height of the triangle:"))
  area = 0.5*base*height
print("the area of triangle is", area)

