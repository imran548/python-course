# # loops help you do some things again and again as long a condition is true
# # loops also help you traverse an iterable object like an array
# # lets start with a while
# # declate loop variable
# # while <condition depending on variable>:
# #   update variable
# #
# #  a loop as a initializer
# i = 0
# # a condition
# while(i < 10):
#     print("i = "+str(i))
#     # an update
#     i += 1
# # an infinite loop case
# # while (True):
#     # print("i is true")
#
# # other type of loop is a for loop, a little more neat than a while loop
# # for <iterating_number_variable> in <a range or an array>
# #       <body>
# #
# #
# for i in range(10):
#     print("i = "+str(i))
#     # range returns a sequence of numbers
# # range( start, stop, step)
# # if you give only one parameter to the function its step is 1 and starts from 0
# for i in range(4, 10):
#     print("i = "+str(i))
#
# for i in range(4, 10, 2):
#     print("i = "+str(i))
# # iterating over an array
# # for loops are used to iterate over arrays
# numbers = [1234, 421, 3, 124, 12, 312, 41, 23, 214, 21, 3]
# for num in numbers:
#     print(num)
# # for loops can also be used to iterate over dictionaries
# dictionary = {
#     "name": "jacky",
#     "state": "stable"
# }
# for key in dictionary:
#     print(dictionary[key])
#
#
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")


# weight = float(input("input your weight"))
# height = float(input("input your height"))
#
# BMI = weight/(height*height)
# print("your BMI is ",round(BMI,2),sep="= ")
# if BMI < 18.5:
#     print("not good")
# elif 18.5< BMI <=24:
#     print('normal')
# elif 24< BMI <=30:
#     print('fat')
# else:
#     print('very fat'


#  #while_loop
# x = 0
# people = []
# while x < 5:
#     person = input("type 5 names")
#     people.append(person)
#     x = x + 1
# print

# password = 84
# pass_ = int(input("input_your_pass"))
# i = 0
# while i < 4:
#     if pass_ == password:
#         break
#     else:
#         pass_ = int(input("wrong pass.input_your_pass"))
#     i = i + 1
# print("try 30 min later")

#for_loop

# keywords = ["top 10 smart phones",'how to track a cell phone', "",'who invented cell phone','how to track a cell phone without them knowin']
# for keyword in keywords:
#     if keyword == "":
#         continue
#     print(keyword)


# keywords = {"phone":["top 10 smart phones",'how to track a cell phone', "",'who invented cell phone',
#                      'how to track a cell phone without them knowin'],
#             "camara":["best camara 2023","best camara under 500"]}
# for catagories in keywords:
#     print("post about",catagories)
#     for keyword in keywords[catagories]:
#         print(keyword)


# import random
# x = 0
# people_list = []
# while x < 8:
#     names = input("enter the names")
#     people_list.append(names)
#     x = x + 1
# index = random.randint(0,7)
#
# select  = people_list[index]
# print(select)



# i = 1
# while i <=5:
#     print("imran :", end="")
#     j =1
#     while j <= 4:
#         print("good",sep="*",end="*")
#
#         j = j +1
#     i = i + 1
#     print()
# print()



# av =10
# x = int(input("canday amount"))
# i = 1
# while i <=x:
#     if i > av:
#         print("out of stock")
#         break
#     print("candy")
#     i = i + 1
# print("have a good day")

# av =10
# x = int(input("canday amount"))
# if x > av:
#     print("out of stock")
# else:
#     i = 1
#     while i <= x:
#
#         print("candy")
#         i = i + 1
#
# print("good day")

# #dont work--------------------------
# for i in range(1-200):
#     if i%3 == 0 and i%5 == 0:
#         continue
#     print(i)
#------------------------------------
#
# continue and pass, skip those--skip others
# XOXOXOXO
# OXOXOXOX
# XOXOXOXO
# for i in range(8):
#     for j in range(8):
#         if (i+j) % 2 == 0:
#             print("X", end="")
#         else:
#             print("O",end="")
#     j = j + 1
#     print()
# i = i +1

#--------------------------------

