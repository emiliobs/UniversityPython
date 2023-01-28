#  Loop Through a List, used a for loop



myList = ["Apple", "Banana","Cherry"]

for fruit in myList:
    print(fruit)


print("=======================================================================")

#   Loop Trought the Index Numbers:


for i in range(len(myList)):
    print(myList[i])

print("=======================================================================")

#  Using a While Loop

i = 0
while i < len(myList):
    print(myList[i])
    i += 1

print(i)
print("=======================================================================")

#  Looping Using List Comprehension:
[print(x) for x in myList]

print("=======================================================================")

# List Comprehension
print("List Comprehension")
fruits = ["apple", "banana","chery", "kiwi", "mango"]
newList=[]

for x in fruits:
    if "a" in x:
        newList.append(x)


print(newList)

print("=======================================================================")

# just one line of code:
print("just one line of code")
newList = [x for x in fruits if "a" in x]

print(newList)


print("=======================================================================")
# Condiction:
print("COndiction")

newList1 = [x for x in fruits if x != "apple"]
print(newList1)

print("=======================================================================")

# with no id statement
print("With no if statement")
newlist2 = [x for x in fruits]

print(newlist2)

print("=======================================================================")

# Iterable
print("iterable")
newList3 = [x for x in range(10)]
print(newList3)

print("=======================================================================")
# iterable with condition
print("Iterable with condition")
newlist4 = [x for x in range(10) if x < 5]
print(newlist4)

print("=======================================================================")

newlis5 = [x.upper() for x in fruits ]
print(newlis5)


print("=======================================================================")

newlist6 = ["HEllo" for x in fruits]
print(newlist6)
print("=======================================================================")

newList7 = [x if x != "banana" else "orange" for x in fruits]
print(newList7)
print("=======================================================================")
print("=======================================================================")
print("=======================================================================")
print("=======================================================================")
print("=======================================================================")
print("=======================================================================")
print("=======================================================================")



