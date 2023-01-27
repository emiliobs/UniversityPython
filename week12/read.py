import os
# f = open("demofile.txt", "r")
# print(f.read())

# f = open("demofile.txt", "r")
# print(f.read(5))

# f = open("demofile.txt","r")
# print(f.readline())
# print(f.readline())

# f = open("demofile.txt", "r")
# for x in f:
# 	print(x)

# f = open("demofile.txt", "r")
# print(f.readline())
# f.close()

# f =open("demofile.txt", "a")
# f.write("Now i love you Emilio, please miss me, today, tomorrow and forever....")
# f.close()

# # open and read the file after the appreding.
# f = open("demofile.txt", "r")
# print(f.read())

# f = open("demofile.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the overwriting.
# f = open("demofile.txt", "r")
# print(f.read())
# f = open("myfile.txt", "x")
# f = open("myfile.txt", "w")

# os.remove("mifile.txt")

#Check if file exist, then delete it.

# if os.path.exists("demofile.txt"):
# 	os.remove("demofile.txt")
# else:
# 		print("The file does not exist.")


# for delete a folders
os.remove("delete/delete.py")
print("archivo eliminado")
os.rmdir("delete")
print("Folder deleted")
