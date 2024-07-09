#write a program to find maximum of three numbers in python 
def maximum_num(val1,val2,val3):
    if val1>val2 and val1>val3:
        print(val1,"is the gretest number")
    elif val2>val1 and val2>val3:
        print(val2,"is the greatest number")
    else:
        print(val3,"is the greatest number")
maximum_num(12,45,15)

#write a python function to create and print a list where the values are sqaure of numbers between 1 and 30.
def create_list():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())

#write a python function that takes a number as a parameters and if the number is prime or not.
def check_prime(num):
    if num == 1:
        print("it is not a prime number")
    if num ==2:
        print("it is a prime number")
    for i in range (2,num):
        if num %i==0:
            print("it is not a prime number")
            break
        else:
            print("it is a prime number")
        break        
check_prime(33)            

#write a python function to sum all the number in a list 
def add(numbers):
    total=0
    for i in numbers:
        total=total+i
    return(total)
print(add([12,4,5,6,7,8]))    

#write a python program to solve the fiboniacci sequence using recursion 
def fs(num):
    if num == 1:
        return(0)
    elif num ==2:
        return(1)
    else:
        return(fs(num-1)+fs(num-2))
print(fs(7))    
