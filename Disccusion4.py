print()
print("Show the string that would result from each of the following string for matting operations. \n If the operation is not legal, explain why.")
print()
print('A - " Looks l ike {1} and {0} for breakfast " . format ( " eggs " , " spam" )')
print("Look like {1} and {0} for breakfast".format("egg", "spam"))

print("====================================================")
print('B - " There is {0} {1} {2} {3}" . format ( 1 , " spam" , 4 , " you" )')
print("There is {0} {1} {2} {3}".format(1, "spam", 4, "you"))

print("====================================================")
print('C - " Hello {0} " . format ( " Susan" , " Computewell "')
print("Hello {0}".format("Susan", "Computewell"))

print("====================================================")
print('D - " {0 : 0 . 2f} {0 : 0 . 2f}" . format (2 . 3 , 2 . 3468)')
print("{0:0.2f} {0:.2f}".format(2.3, 2.3468))

print("====================================================")
print('E - " {7 . 5f} {7 . 5f} " . format (2 . 3 , 2 . 3468)')
#print("{7.5f} {7.5f}".format(2.3, 2.3468))
print("IndexError: Replacement index 7 out of range for positional args tuple , Error -- Missing position specifier (or leading :)")

print("====================================================")
print('Time left {0 : 02} : {1 : 05 . 2f } " . format ( 1 , 37 . 374)')
print("Time left {0:02}:{1:05.2f}".format(1, 37.374))


print("====================================================")
print('G - {1 : 3} " . format ( " 14" )')
#print("{1:3}".format(14))
print("IndexError: Replacement index 1 out of range for positional args tuple Error - There is no argument 1")



