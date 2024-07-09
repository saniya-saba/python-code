# a = "OTD.YOLO.ASAP.BRB.GTG.OTW"
# #write a program to seprate the following string into coma(,) seprated values
# b=a.split(".")
# print(b)
# #write a program to sort strings alphabetically in python 
# b=sorted(a)
# print(b)
# #write a program to remove a given character from a string 
# b=a.replace("OTD","SABA")
# print(b)
# #write a program to remove the dot(.) from the following string
# b=a.replace("."," ")
# print(b)
# #write a program to check the number of accurance of a substring in a string
# b=a.count("O")
# print("the number of times substring sea is occuring is:",b)

#take an input from a user as a string then reverse it 
a=input("enter anthing here:")
# print(a[::-1])
#write a program to check if a string conatins only digits.
# b=(a.isdigit( ))
# if b == True:
#   print("it contains only digits")
# else:
#   print("it does not contain only digits")

#write a program to to check if string is palindrome.
# rev = a[:: -1]
# if a == rev:
#   print("it is palindrome")
# else:
#   print("it is not a plindrome")

#write a program to find number pf vowels in a string 
# vowels = 0
# for i in a: 
#   if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#     print("the number of vomels in the following string is are", vowels) 
# else:
#   print("the number string is not in following list")

#write a program to check if every words= in a string begins with a capital letter
print(a.istitle())


