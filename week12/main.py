# def main():
# 	fname = input("Enter Filename: ")
# 	infile = open(fname, 'r')
# 	data = infile.read()
# 	print(data)

# # main()
# def main():
# 	fname = input("Enter Filename: ")
# 	infile = open(fname, "r")
# 	for i in range(5):
# 		line = infile.readline()
# 		print(line[:-1])


# main()

def main():
			print("This program creates a file of username from a file of name.")

	# get  the file names
			infileName = input('What file are the name in? ')
			outfileName = input("What file should the username go in? ")

		  

	  # open the files
			infile = open(infileName, "r")
			outfile = open(outfileName, "w")


       

	  # process each line of the input file
			for line in infile:

					# print(line)

					# input()
		# Get the first and last names form line
					first = line.split()
					last = line.split()


					# print(first,)
					# print(first, last)
		# Write it to the output filedemo
					uname = (str(first[0] )+ str(last[:7])).lower()

					print(uname, file=outfile)


    # close both files.

			infile.close()
			outfile.close()
      
			print(f"Username  have been writte to {outfileName}")

main()