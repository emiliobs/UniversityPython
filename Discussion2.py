s1 = "spam"
s2 = "ni!"
print()
print("Given the same initial statements  as in the previous problem,\n show a Python expression that could contruct each of the following \n result by preforming string operation on s1 and s2")
print()
print(f"1. Given the initial statements of s1 = {s1} and s2 = {s2}")
print()

print("=========================================================")
print("A")
print(s2[0:2].upper())

print("=========================================================")
print("B")
print(s2 + s1 + s2)

print("=========================================================")
print("C")
print((s1.capitalize().ljust(4) + s2.capitalize().ljust(4)).ljust(5) * 3)

print("=========================================================")
print("D")
print(s1)

print("=========================================================")
print("E")
print(s1.split("a"))

print("=========================================================")
print("F")
print(s1[0:2] + s1[3])



