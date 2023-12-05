# import random
# list=["python","php","java","c++"]
# print(list)
# random.shuffle(list,random.random)
# print(list)
#
# print("____________________")
# list2=["canada","USA","UK","China"]
# list3=["brazil","Germany"]
# list4=list2+list3
# mergedlist=[]
# mergedlist.extend(list2)
# mergedlist.extend(list3)
# print(mergedlist)

rides = [
    ["Roller Coaster", 120, 10],
    ["Ferris Wheel", 100, 5],
    ["Bumper Cars", 90, 4]
]

# User's details:
user_height = 115  # in cm
user_age = 9  # in years

# Checking for Roller Coaster:
if user_height >= rides[0][1] and user_age >= rides[0][2]:
    coaster_status = "can ride"
else:
    coaster_status = "can't ride"

# Checking for Ferris Wheel:
if user_height >= rides[1][1] and user_age >= rides[1][2]:
    wheel_status = "can ride"
else:
    wheel_status = "can't ride"

# Checking for Bumper Cars:
if user_height >= rides[2][1] and user_age >= rides[2][2]:
    bumper_status = "can ride"
else:
    bumper_status = "can't ride"

print(f"The user {coaster_status} the Roller Coaster.")
print(f"The user {wheel_status} the Ferris Wheel.")
print(f"The user {bumper_status} the Bumper Cars.")