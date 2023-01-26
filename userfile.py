# def main ( ) :
print ("This program creates a f ile of usernames from a")
print ("file of names. ")
# get the f ile names
infileName = input ("What f ile are the names in? ")
outfileName = input ("What f ile should the usernames go in? ")
# open the f iles
infile = open(infileName, "r")
outfile = open(outfileName , "w")
# process each l ine of the input f ile
for line in infile:
# get the f irst and last names from line
    first, last = line.split()
# create the username
    uname = (first[O] + last[:7]).lower()
# write it t o the output f ile

    print (uname , file=outfile)
# close both f iles
infile.close ()
outfile.close ()
print ("Usernames have been written t o " , outfileName)
main ()