# EXERCISE 14
# Write a program that finds the average of a series of numbers entered by 
# the user. As in the previous problem, the program will first ask the user 
# how many numbers there are. Note: The average should always be a float, 
# even if the user inputs are all ints.
 #averageSeriesOfNumber.py
 
def main():
    print("Start")
    print("This program to find the average pf series of number.")
    print()
     
    insert_notas = int(input("How many number do you have?: "))
    total = 0
    for i in range(insert_notas):
        notes =  float(input("Insert Notes to find average: "))
        total = total + notes
    print(f"The average of {insert_notas} notes is: {total / insert_notas}")
    print("End")
        
        
main()    