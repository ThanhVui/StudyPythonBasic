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

# set1 = set(("apple", "banana", "cherry", True, 1, "apple", False, 0))
# print(set1)