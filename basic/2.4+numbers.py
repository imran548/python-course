# Operator	Name	Example	Try it
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y

#==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y

# Identity Operators
# is 	Returns True if both variables are the same object	x is y
# is not	Returns True if both variables are not the same object	x is not y

#
# in 	Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y


# numbers can be of 3 types
# dynamically typed language, on run time the type is checked by the compiler
integer_num = 23
float_num = 23.233333
complex_num = 23j
# we dont use complex numbers a lot in this course so we will end the discussion on them here
# OPERATIONS
# addition
x = 23
y = 2
addition = x + y
print(addition)
# subtraction
subtraction = x - y  # 21
# multiplication
multiplication = x * y  # 46
# division
# there are two types of divisions inn python, one is called floor division and the other is simple division
# simple division
div_simple = x / y  # 11.5
print(div_simple)
# floor division is simply the same division without the decimal part {the part after the point}
div_floor = x // y  # 11
print(div_floor)
# modulus operator
mod = x % y  # 1 returns the remainder after dividing x by y
print(mod)


