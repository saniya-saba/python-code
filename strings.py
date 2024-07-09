# #string manipulation
# a="hello world!"
# print(type(a))
# print(a)
# print(len(a)) #length
# print(a.count("0")) #conut
# print(a.upper()) #upper
# print(a.lower()) #lower
# #print(a.index("0")) #index
# print(a.capitalize()) #capitaluze
# print(a.find("o")) ##find
# print(a.format()) #format
# name="saniya"
# print(name.center(20 ,"*")) #center
#string function
# a="hello"
# b="Hello123"
# c="12345"
# d="HELLO"
# e=" "
# f="Hello 123@"
# g="1.234"
# h="Harry Potter And The Numaric Values"
# #isalnum
#print(a,":",a.isalnum())  #true 
#print(b,":",b.isalnum())  #true
#print(c,":",c.isalnum())  #true
#print(d,":",d.isalnum())  #true
#print(f,":",f.isalnum())  #false
#isalpha
# print(a,":",a.isalpha())#true
# print(b,":",b.isalpha())#false
# print(c,":",c.isalpha())#false
# print(d,":",d.isalpha())#true
#isdecimal
# print(a,":",a.isdecimal()) #false
# print(b,":",b.isdecimal())#false
# print(c,":",c.isdecimal())#true
# print(d,":",d.isdecimal())#false
#isdigit
# print(a,":",a.isdigit())#false
# print(b,":",b.isdigit())#false
# print(c,":",c.isdigit())#true
# print(g,":",g.isdigit())#false
#isnumaric
# print(a,":",a.isnumeric()) #false
# print(c,":",c.isnumeric())#true
#islower
# print(a,":",a.islower()) #true
# print(d,":",d.isnumeric()) #false
#isupper
# print(a,":",a.isupper()) #false
# print(d,":",d.isupper()) #true
#isspace
# print(a,":",a.isspace())#false
# print(e,":",e.isspace())#true
#istitle
# print(a,":",a.istitle())#false
# print(f,":",f.istitle())#true
# print(h,":",h.istitle())#true

#string function
#endwith
# a="saniya saba"
# print(a,":",a.endswith("a"))#true
# print(a,":",a.endswith("i",2,8))#false
#startwith
# a="saniya saba"
# print(a,":",a.startswith("s"))#true
# print(a,":",a.startswith("s",3,6))#false
#swapcase
# a="saniya saba"
# print(a,":",a.swapcase()) #SANIYA SABA
# a=" ********       saniya saba.        ********"
# print(a,":",a.strip())
# print(a,":",a.strip(".,*, "))
#ljust
# a="saniya saba"
# x=a.ljust(20) 
# print(x,"ths is my name")
# y=a.ljust(20,"*")
# print(y,"this is my name")

#Rjust
# a="saniya saba"
# x=a.rjust(20,"-") 
# print(x,"she is pretty gril")
#rindex
# a="saniya saba is pretty girl and she is smart."
# print(a.rindex("saba"))
# #rfind
# print(a.rfind("girl"))
# print(a.rfind("a",0,9))

#slicing in string
a="saniya saba is pretty girl and she is smart."
b="123456789"
print(a)
print(a[0:6])
print(a[-6:])
print(b[::2])
print(b)
print(b[::-1])
print(b[:7:2])





