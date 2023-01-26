# EXERCISE 13
 # Write a program to sum a series of numbers entered by the user. The 
 # program should first prompt the user for how many numbers are to be 
 # summed. The program should then prompt the user for each of the numbers i
 # n turn and print out a total sum after all the numbers have been 
 # entered. Hint: Use an input statement in the body of the loop.
  # to find the sum a series of number entered by the user:
   #sumSeriesOfNumber.py  
def main():
    print("Start")
    print("This program find the sum a series of the number entered for the user")
    print()
    
    number_to_sum = int(input("Enter how many number Do you want to sum?: "))
    total_sum = 0
    for i in range(number_to_sum):
        get_sum_number = float(input("Enter number to sum: "))
        total_sum = total_sum + get_sum_number
    
    print()
    print(f"The sum of the {number_to_sum} numbers,  is: {total_sum}")
    print("End")   
   

main()      