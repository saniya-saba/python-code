##write a program to check if a number is positive or not
'''num=int(input("enter a number here:"))
if num>0:
    print("it is positive")
else:
    print("it is negative")'''
#write a program to check whether a number is odd or even
'''num=int(input("enter a number here:"))
if num%2==0:
    print(" it is an even number")
else:
    print("it is odd number")'''
#write a program to create area calculator

'''print("****AREA CALCULATOR****")
print(""" press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
 press 4 to get the area of triangle""")
choice=int(input("enter a number between 1-4:"))
if choice==1:
    side=float(input("enter the length of one side:"))
    area=side**2
    print("the area of square is",area)
elif choice == 2:
    length = float(input("enter the length of the rectangle:"))
    width = float(input("enter the width of the rectangle:"))
    area = length*width
    print("the area of the rectangle is:",area)
elif choice == 3:
    radius = float(input("enter the radius of the circle:"))
    area = ((22/7)*(radius))
    print("the area of the circle is", area)
elif choice == 4:
    base = float(input("enter the base of the triangle:"))
    height = float(input("enter the height of the triangle:"))
    area = 0.5*base*height
    print("the area of the triangle is:", area)
else:
    print("invalid input")'''
#write a program check whether the passed letter is vowel or not
'''letter=input("enter a letter here:")
if(letter in "aeious") or (letter in "AEIOUS"):
    print("it is a vowel")
else:
    print("it is not a vowel")'''
#write a program to check if a number is a single digit number 2-digit number and soon.... upto 5digit
num=int(input("enter a number upto 5 digits:"))
if num>=0 and num<=9:
    print("it is single digit number")
elif num>=10 and num<=99:
    print("it is double digit number")
elif num>=100 and num<=999:
    print(" it is triple digit number")
elif num>=1000 and num<=9999:
    print("it is four digit value")
elif num>=10000 and num<=99999:
    print("it is five digit value")
else:
    print("invalid input")
