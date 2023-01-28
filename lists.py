# mylist = ["apple", "banna", "cherry"]
# print(mylist)
# thislist = ["apple","banana","cherry","apple","cherry"]
# print(thislist)
#len() function to the termine how manu otems a list has.

# myList = ["apple","banana","cherry"]
# print(len(myList))

# list item - data type
# list1 = ["apple", "banana","cherry"]
# list2 = [1,2,3,4,5]
# list3 = [True, False, True, False]
# list4  = ["abc", "55", True, 50, False, "value"]

# print(type(list1))
# print(type(list2))
# print(type(list3))
# print(type(list4))

# the list() constructor
# myList = list(("apple","banan","cherry"))
# print(myList)
# print(myList[1])
# print(myList[-2])
# myList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# print(myList[2:5])
# print(myList[0])
# print(myList[:4])
# print(myList[2:])
# print(myList[-4:-1])
# #=
# # Check if the Item exists
# if "Emilio" in myList:
# 	print("Yes, 'Emilio is in the fruits list.")
# else:
# 	print("Sorry!, this man is down!")	

# Change Item Value
# 	chgange the second item:
# myList[1] = "Marranos"
# print(myList)

#  Change a Range of item values:
#     change the vlaues "bananas" and cherry with the values "blackcurrant" and watermelon
# myList[1:3] = ["blackcurrant", "watermelon"]
# print(myList)

# Change the second values by replacing it with two nr=ew values
# myList[1:2] = ["marranos", "cerdos"]
# print(myList)

#  Change the second and third value by replacing it with one value
from cgi import print_environ


#myList = ["apple", "banana", "cherry"]
# myList[1:3] = ["watermelon"]
# print(myList)

#Insert Items
#myList.insert(2,"marranos")
#print(myList)

## NOte: aqui voy - https://www.w3schools.com/python/python_lists_add.asp

# Add List Item
#  used the append()

#
#myList.append("orange")
#print(myList)

# used the insert item
# insert() method

#myList.insert(1,"Pasio fruit")
#print(myList)

# Extend List, used the extend() method.
#tropical = ["mango","pineaple", "papaya"]
#myList.extend(tropical)
#print(myList)

#Add nay iterable with extend() method
#myDupla = ("Kiwi", "orange")
#myList.extend(myDupla)
#print(myList)

# Remove Listr Items
#   use the remove() method removes the specified item
#myList.remove("banana")
#print(myList)

#  remove Specified Index
# use the pop() method removes the specified inds.
#myList.pop(1)
#print(myList)
myList = ["apple", "banana", "cherry"]
#myList.pop()
#print(myList)
#del myList[0]
#print(myList)

# Clear the Lisyt, use the clear() method emties lisyt
myList.clear()
print(myList)