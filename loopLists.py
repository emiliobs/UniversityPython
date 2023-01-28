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

# i am here https://www.w3schools.com/python/python_lists_comprehension.asp
print("=======================================================================")


