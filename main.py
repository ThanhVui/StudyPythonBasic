# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import sys

# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    # print data
# print("Hello Word!")
# print(sys.version)

    # if statement
# if 5 > 2:
#     print("That's right!")
# if 5 > 2:
#         print("That's right!")

    # Variable
# x = 5
# y = "Hello, World!"

"""
This is comment
more than one
line
"""
from itertools import count
from time import process_time
from tkinter.font import names

# x = 5
# y = 10
# print("Multiplie: x * y = " + str(x * y))

"""
- in python either use single or double quotes
- in python variable name are case-sensitive (not ignore uppercase or lowercase)
"""
# x = 3
# y = "Vui"
# z = 4
# Z = 39
# print(str(3))
# print(str(y))
# print(float(z))
# print(int(z))
# print(Z)
#
# print(type(x))
# print(type(y))
# print(type(z))

"""
- there are three rules to put name for variable
    + camelCase: myVariable = "Vui"
    + PascalCase: MyVariable = "Vui"
    + SnakeCase: my_variable = "Vui"
"""

"""
assign multiple value
"""
# a, b, c = "Vui", 3, "Happy"
# print(a, b, c)
# print(type(a), type(b), type(c))
#
# x = y = z = "Assign Multiple Value"
# print(x, y, z)

"""
unpack a collection
"""
# fruits = ["apple", "banana", "cherry"]
# e, f, g = fruits
# print(e, f, g)

"""
you can also use the '+' or ',' operator to output multiple values
"""
# x = "Python"
# y = "Is"
# z = "Happy"
# print(x, y, z)
# print(x + " " + y + " " + z)

"""
operator
"""
# x = 4
# y = 3
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y) # remainder

# x = 4
# y = "Vui"
# print(x, y)

"""
function print function basic
"""

# def myName(name):
#     print("My name is " + name)
#
# def myFullName(firstName, lastName):
#     print("My full name is " + firstName + " " + lastName)
#
# myName("Vui")
# myName("Happy")
# myFullName("Vui", "Thanh")

"""
global variable
"""
# x = "Thanh Vui"
# def myGlobalVariable():
#     x = "Happy"
#     print(x)
# myGlobalVariable() #"Happy"
# print(x) #"Thanh Vui"

# def myGlobal():
#     global x
#     x = "Thanh Vui"
# myGlobal()
# print(x)

# x = "Thanh Vui"
# def myGlobalVariable():
#     global x
#     x = "Happy"
#     print(x)
# myGlobalVariable() #"Happy"
# print(x) #"Happy"

"""
data types
"""
# x = None
# print(type(x))
# print(x)

# x = 1
# y = 32840924830984092480980943859035803508380958580385903
# z = -3255522
# print(type(x))
# print(type(y))
# print(type(z))

# x = -87.7e100
# print(type(x))# print(x)

# x = 3 + 5j
# print(type(x))
# print(x)

# x = 3.3
# print(int(x))

# import random
# print(random.randrange(1, 5))

# a = '''thanh
# vui
# tang'''
# b = """\nthanh
# vui
# tang"""
# print(a, b)

# a = "Thanh, Vui"
# print(a[3])

# count = 0
# for x in "ThanhVui":
#     # count += 1
#     print(x)
# # print(count)

"""
to get the length of string use len()
"""
# a = "This is a string"
# print(len(a))

"""
check string in sequence
"""
# a = "Thanh Vui Handsome"
# print("Vui" in a)
# if "Vvi" in a:
#     print("Yes, 'Vui' in this text!")
# else:
#     print("No, 'Vui' not in this text!")
#
# if "vui" not in a:
#     print("Yes, 'Vui' not in this text!")
# else:
#     print("No, 'Vui' in this text!")

# a = "Thanh Vui Handsome"
# print(a[-5:-2])

# a = "  Thanh, Vui, Handsome  "
# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.replace("Vui", "Happy"))
# print(a.split(", "))

# name = "Vui"
# age = 21
# a = 2
# b = 4
# price = 2.9039082
# txt = f"My name is {name}.\nI'm {age} years old.\n{a * b}\n{price:.3f}"
# print(txt)

# a = "this is a string"
# print(len(a))
# print(a.center(100, " "))
#
#
# txt = "banana"
#
# x = txt.center(20, "O")
#
# print(x)

# print(bool(""))
# print(bool(0))

# a = 200
# print(isinstance(a, int))

"""
operators
"""
# print(3 ** 3) # exponentiation
# print(19 % 3) # modulus
# print(19 // 3) # floor division

# a = 5 # 0101
# b = 3 # 0011
# a &= b # 0001
# print(a) # 0001 = 1
#
# a = 5 # 0101
# b = 3 # 0011
# a |= b # 0111
# print(a) # 0111 = 7
#
# a = 5 # 0101
# b = 3 # 0011
# a ^= b # 0110
# print(a) # 0110 = 6
#
# a = 5 # 0101
# a >>= 2 # 0001
# print(a) # 0001 = 1
#
# a = 5 # 0101
# a <<= 2 # 0100
# print(a) # 01 0100 = 4


"""
list
"""
# there is two ways to create a list use ["java", "python", 12] or list(("java", "python", 12))
# myList = ["java", "python", 12]
# print(type(myList))
#
# myList = ["java", "python", 12, "dart", "javascript", "kotlin"]
# print(myList[3])
# print(myList[-1])
# print(myList[-2])
# print(myList[2:4])

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "mango")
# thislist.append("orange")
# print(thislist)

# thisList = ["apple", "banana", "cherry"]
# thatList = ["mango", "orange", "lemon"]
# thatList.extend(thisList)
# print(thatList)

# thisList = ["apple", "banana", "cherry"]
# thatList = ("mango", "orange", "lemon")
# thisList.extend(thatList)
# print(thisList)

# thislist = ["apple", "banana", "cherry"]
# # thislist.remove("banana")
# # thislist.pop(0)
# # del thislist[2]
# # del thislist
# # thislist.clear()
# # print(thislist)
# print(range(len(thislist)))
# # for item in range(len(thislist)):
# #     print(thislist[item])

# thislist = ["apple", "banana", "cherry"]
# # i = 0
# # while i < len(thislist): # 1 < 3 (0, 1, 2)
# #     print(thislist[i])
# #     i += 1
#
# [print(x) for x in thislist]

"""
list comprehension
"""
# thatList = ["mango", "orange", "lemon"]
# newList = []
# for x in thatList:
#     if "a" in x:
#         newList.append(x)
#
# print(newList)

# short hand
# thatList = ["mango", "orange", "lemon"]
# newList = [x for x in thatList if "a" in x]
# print(newList)

# newList = [x for x in range(10)]
# print(newList)

# newList = [x for x in range(10) if x > 3]
# print(newList)

# thatList = ["mango", "orange", "lemon"]
# newList = [x.upper() for x in thatList]
# print(newList)

# thatList = ["mango", "orange", "lemon"]
# newList = ["Vui" for x in thatList]
# print(newList)

# thatList = ["mango", "orange", "lemon"]
# newList = [x if x != "mango" else "apple" for x in thatList]
# print(newList)

# thatList = ["mango", "orange", "lemon"]
# thatList.sort()
# print(thatList)

# numList = [2, 1, 7, 3, 6, 5, 0]
# numList.sort()
# print(numList)

# numList = [2, 1, 7, 3, 6, 5, 0]
# numList.sort(reverse = True)
# print(numList)

# def myfunc(n):
#   return abs(n - 50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)  # 50, 0, 15, 32, 27
# print(thislist) # 50, 65, 23, 82, 100

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.reverse()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# newList = thislist.copy()
# print(newList)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# newList = thislist[:]
# print(newList)

"""
tuple
"""
# myTuple = ("apple", "banana", "cherry")
# firstTuple = ("apple",)
# tuple2 = tuple(("apple", "banana", "cherry"))
# print(myTuple)

# convert from tuple to list and convert list to tuple to change tuple
# tuple1 = ("apple", "banana", "cherry")
# list1 = list(tuple1)
# list1[2] = "mango"
# tuple1 = tuple(list1)
# print(tuple1)

# add items into tuple
# tuple1 = ("apple", "banana", "cherry")
# list1 = list(tuple1)
# list1.append("mango")
# tuple1 = tuple(list1)
# print(tuple1)

# add tuple to tuple
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = ("mango",)
# tuple1 += tuple2
# print(tuple1)

# remove items in tuple
# tuple1 = ("apple", "banana", "cherry")
# list1 = list(tuple1)
# list1.remove("apple")
# tuple1 = tuple(list1)
# print(tuple1)

# unpacking a tuple
# tuple1 = ("apple", "banana", "cherry")
# (item1, item2, item3) = tuple1
# print(item1)
# print(item2)
# print(item3)

# tuple1 = ("apple", "banana", "cherry", "mango")
# (item1, item2, *item3) = tuple1
# print(item1)
# print(item2)
# print(item3)

# tuple1 = ("apple", "banana", "cherry", "mango")
# (item1, *item2, item3) = tuple1
# print(item1)
# print(item2)
# print(item3)

# loop tuple
# tuple1 = ("apple", "banana", "cherry", "mango")
# for item in tuple1:
#     print(item)

# loop use rang and len
# tuple1 = ("apple", "banana", "cherry", "mango")
# for item in range(len(tuple1)):
#     print(tuple1[item])

# while loop
# tuple1 = ("apple", "banana", "cherry", "mango")
# item = 0
# while item < len(tuple1):
#     print(tuple1[item])
#     item += 1

# join two tuple
# tuple1 = ("apple", "banana", "cherry", "mango")
# tuple2 = ("lemon",)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# tuple1 = ("apple", "banana", "cherry", "mango")
# tuple2 = tuple1 * 2
# print(tuple2)


"""
sets
"""
# mySets = {"apple", "banana", "cherry"}
# print(mySets)
#
# set1 = set(("apple", "banana", "cherry", True, 1, "apple", False, 0))
# print(set1)

# mySets = {"apple", "banana", "cherry"}
# mySets.add("mango")
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# sets2 = {"pineapple", "mango", "lemon"}
# mySets.update(sets2)
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# sets2 = ["pineapple", "mango", "lemon"]
# mySets.update(sets2)
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# mySets.remove("banana")
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# mySets.discard("banana")
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# x = mySets.pop()
# print(x)
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# mySets.clear()
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# for item in mySets:
#     print(item)


# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"pineapple", "mango", "lemon"}
# sets3 = {"orange",}
# sets4 = {"nana"}
# sets5 = sets1.union(sets2, sets3, sets4)
# print(sets5)

# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"pineapple", "mango", "lemon"}
# sets3 = {"orange",}
# sets4 = {"nana"}
# sets3 = sets1 | sets2 | sets3 | sets4
# print(sets3)

# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"pineapple", "mango", "lemon"}
# sets3 = {"orange",}
# sets4 = {"nana", "banana", "cherry"}
# sets5 = sets1.intersection(sets4)
# print(sets5)

# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"pineapple", "mango", "lemon"}
# sets3 = {"orange",}
# sets4 = {"nana", "banana", "cherry"}
# sets5 = sets1 & sets4
# print(sets5)

# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"banana", "mango", "lemon"}
# sets5 = sets1.intersection_update(sets2)
# print(sets5)

# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"banana", "mango", "lemon"}
# sets5 = sets1.difference(sets2)
# print(sets5)

# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"banana", "mango", "lemon"}
# sets5 = sets1 - sets2
# print(sets5)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print(set1)

"""
dictionaries
"""
# dict1 = {
#     "brand": "ford",
#     "model": "Mustang",
#     "year": 1999
# }
# print(dict1)

# get the value of key through [key]
# dict1 = {
#     "brand": "ford",
#     "model": "Mustang",
#     "year": 1999
# }
# print(dict1["model"])

# dict1 = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(dict1)

# dict use dict()
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# print(dict1)

# how to get value from key
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# x = dict1.get("name")
# print(x)

# how to get key from value
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# x = dict1.keys()
# print(x)

# how to change
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# x = dict1.keys()
# print(x)
# dict1["color"] = "red"
# print(x)

# how to change
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# x = dict1.values()
# print(x)
# dict1["color"] = "red"
# print(x)

# how to change
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# x = dict1.items()
# print(x)
# dict1["color"] = "red"
# print(x)

# how to change value of key
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# dict1["name"] = "Happy"
# print(dict1)

# how to change value of key
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# dict1.update({"name": "Happy"})
# print(dict1)

# how to change value of key
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# dict1.pop("name")
# print(dict1)

# how to change value of key
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# dict1.pop("name")
# print(dict1)

# how to remove item
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)

# how to loop through dict
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# for item in dict1:
#     print(dict1[item])

# how to loop through dict
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# for item in dict1.values():
#     print(item)

# how to loop through dict
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# for item in dict1.keys():
#     print(item)

# how to loop through dict
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# for key, value in dict1.items():
#     print(key, value)

"""
nested dictionary
"""
# mydict = {
#     "dict1": {
#         "name": "John",
#         "age": 30
#     },
#     "dict2": {
#         "name": "Vui",
#         "age": 33
#     },
#     "dict3": {
#         "name": "Happy",
#         "age": 22
#     }
# }
# print(mydict)

# dict into dict
# dict1 = {
#     "name": "John",
#     "age": 30
# }
# dict2 = {
#     "name": "Vui",
#     "age": 33
# }
# dict3 = {
#     "name": "Happy",
#     "age": 22
# }
#
# mydict = {
#     "child1": dict1,
#     "child2": dict2,
#     "child3": dict3
# }
# print(mydict)

# dict1 = {
#     "name": "John",
#     "age": 30
# }
# dict2 = {
#     "name": "Vui",
#     "age": 33
# }
# dict3 = {
#     "name": "Happy",
#     "age": 22
# }
#
# mydict = {
#     "child1": dict1,
#     "child2": dict2,
#     "child3": dict3
# }
# print(mydict["child1"]["name"])

# dict1 = {
#     "name": "John",
#     "age": 30
# }
# dict2 = {
#     "name": "Vui",
#     "age": 33
# }
# dict3 = {
#     "name": "Happy",
#     "age": 22
# }
#
# mydict = {
#     "child1": dict1,
#     "child2": dict2,
#     "child3": dict3
# }
# for item, object in mydict.items():
#     print(item)
#     for child in object:
#         print(item + ":", object[child])

"""
if else statement
if
elif
else
"""
# a = 3
# b = 3
# if a > b:
#     print("a greater than b")
# elif a < b:
#     print("a less than b")
# else:
#     print("a equals b")
#
# if a == b: print("a equals b")

# a = 3
# b = 3
# print("a equal b") if a == b or a < b else print("not equal")

# a = 3
# b = 2
# if b < a:
#     print(a)
#     pass

"""
while and for loop
"""
# i = 1
# while i < 6:
#     print(i)
#     i += 1
#
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")

# for x in range(6):
#     print(x)

# for x in range(2, 6):
#      print(x)

# for x in range(2, 30, 3):
#      print(x)
# else:
#     print("Finally For Loop")


"""
function
"""
# def function1():
#     print("Hello World")
# function1()
# function1()

# def my_function(*kids):
#   for x in kids:
#       print("The youngest child is " + x)
#
# my_function("Emil", "Tobias", "Linus")

# def my_function(**kid):
#   print("His last name is " + kid["fname"])
#
# my_function(fname = "Tobias", lname = "Refsnes")

# def my_function(country = "Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")