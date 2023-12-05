print("hellow world")
print("hello \nworld")
print('TOday\'s weather is cloudy')
print('this is back slash \\')
'''this is comment '''
# this is comment
print('this is imran\t')
print('this is imran\t\t')
print('“He said, ”Hi!”')

#' ' or "" can used in print function
#ARGUMENT
print('THIS IS IMRAN','I LOVE CODING', sep= '-------')
#sep is a seperator operator
print('a','f','r',sep="===", end="+++")
print('a','f','r',sep="===")



#UNDERSTANDING VARIABLES AND DATA TYPES

a = 45
b = 54
print("total",a*b, sep='=')

#variable are case sensative, name can not start with number
# alphabet, _
A = 64
print(a,A)
egg_price = 45#snake case

#Data type
    #string type of data
name = "imran"
print(type(name))
    #boolean data types
print(6>3)
a = True
b = False
print(type(a))

#input function
name = input("please inter your name: ")
number = input("please inter surname name: ")
print('Hi',name,number)

name = input("name:")
profession = input("profession")
age = input("age")
print(name,'is an',profession,'his age is',age)

#data casting
number_of_eggs = int(input('how many eggs you want'))
print("price = ",number_of_eggs*12)
