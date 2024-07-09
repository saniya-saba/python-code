#to display this pattern
'''1
   2 2
   3 3 3
   4 4 4 4
   5 5 5 5 5'''
'''for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()'''
#2 pattern
'''11111
2222
333
44
5'''
'''for i in range(1,6):
    for j in range(6,i,-1):
      print(i,end=" ")
    print()'''
#3pattern
'''     *
       **
      ***
     ****
    *****'''
'''for i in range(1,6):
 for k in range(5,i,-1):
    print("",end=" ")
for j in range(i):
     print("*",end=" ")
     print()'''
#4pattern
'''for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()'''
#5pattern
'''for l in range(6,0,-1):
    for k in range(0,l-1):
        print("*",end=" ")
    print()'''
#6pattern
'''for l in range(6,0,-1):
    for k in range(0,l-1):
        print("*",end=" ")
    print()'''
#7pattern
'''for i in range(1,11):#(1,11)
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()'''