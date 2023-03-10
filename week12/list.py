#Making a list:
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
#Accessing elements:
# Getting the first element
first_col = colors[0]
# Getting the second element
second_col = colors[1]
# Getting the last element
newest_col = colors[-1]
Modifying individual items:
# Changing an element
colors[0] = 'Yellow'
colors[-2] = 'Red'
Adding elements:
# Adding an element to the end of the list
colors.append('Orange')
# Starting with an empty list
colors = []
colors.append('Red')
colors.append('Blue')
colors.append('Green')
# Inserting elements at a particular position
colors.insert(0, 'Violet')
colors.insert(2, 'Purple')
Removing elements:
# Deleting an element by its position
del colors[-1]
# Removing an item by its value
colors.remove('Green')
Popping elements:
# Pop the last item from a list
most_recent_col = colors.pop()
print(most_recent_col)
# Pop the first item in a list
first_col = colors.pop(0)
print(first_col)
List length:
# Find the length of a list
num_colors = len(colors)
print("We have " + str(num_colors) + " colors.")
Sorting a list:
# Sorting a list permanently
colors.sort()
# Sorting a list permanently in reverse alphabetical order
colors.sort(reverse=True)
# Sorting a list temporarily
print(sorted(colors))
print(sorted(colors, reverse=True))
# Reversing the order of a list
colors.reverse()
Looping through a list:
# Printing all items in a list
for col in colors:
 print(col)
# Printing a message for each item, and a separate message afterwards
for col in colors:
 print("Welcome, " + col + "!")
print("Welcome, we're glad to see you all!")
The range() function:
# Printing the numbers 0 to 2000
for num in range(2001):
 print(num)
# Printing the numbers 1 to 2000
for num in range(1, 2001):
 print(num)
# Making a list of numbers from 1 to a million
nums = list(range(1, 1000001))
Simple statistics:
# Finding the minimum value in a list
nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
num_min = min(nums)
# Finding the maximum value
nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
num_max = max(nums)
# Finding the sum of all numbers
nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
total_num = sum(nums)
Slicing a list:
# Getting the first three items
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
first_three = colors [:3]
# Getting the middle three items
middle_three = colors[1:4]
# Getting the last three items
last_three = colors[-3:]
Copying a list:
# Making a copy of a list
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
copy_of_colors = colors[:]
List of Comprehensions:
# Using a loop to generate a list of square numbers
squr = []
for x in range(1, 11):
 sq = x**2
 squr.append(sq)
# Using a comprehension to generate a list of square numbers
squr = [x**2 for x in range(1, 11)]
# Using a loop to convert a list of names to upper case
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
upper_cols = []
for cols in colors:
 upper_cols.append(cols.upper())
# Using a comprehension to convert a list of names to upper case
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
upper_cols = [cols.upper() for cols in colors]