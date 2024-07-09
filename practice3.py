#write a program to find a sum of allthe even number up to 50.
'''sum=0
for i in range(1,51):
    if i%2==0:
        sum+=1
        print(" the sum of all the even number up to 50 is:",sum)'''
#write a program to write a first 20 number and their squared numbers
'''for i in range(1,21):
    print(i,"squre","=",i**2)'''
#write a program to find sum of first 10 odd number using while loop
'''sum=0
n=0
while n<=20:
    if n%2!=0:
        sum+=n
    n+=1
print("the sum of the 10 odd number is:",sum)'''
#write a program to check if a number is divisible by 8 and 12, up to 100 numbers
'''for i in range(1,100):
    if i%8 ==0 and i%12==0:
        print(i)'''
#write a program to create a billing system at supermarket
'''while True:
  name=input("enter customer's name:")
  total = 0
  while True:
    print("enter the amount and quantity")
    amount = float(input("enter amount:"))
    quantity = float(input("enter quantity:"))
    total += amount * quantity
    repeat=input("do want to add more items? (yes/no):")
    if repeat == "no" or repeat == "No":
        break
  print("-"*40)
  print("Name:",name)
  print("amount to be paid:",total)
  print("-"*40)
  print("*******happy shopping*******")
  repeat1=input("do you want to go next customer?(yes/no):")
  if repeat1=="no" or repeat1=="No":
      break
'''
A=" why fit in, when you are born to stand out!"
#finding length
b=(len(A))
print(" the length of the given string is:",b)
#check how many times alphabet o is occuring
print("the number of times o is occuring is :",A.count("o"))
#conveting lower to upper cases
x=A.lower()
print(x)
y=A.upper()
print(y)
#coverting the string into a title
z=A.title()
print(z)
#to find the index number of "fit in"
print(A.find("fit in"))



