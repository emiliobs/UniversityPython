# Execise 11
# Write a program to find the sum of the first n natural numbers, where the 
# value of n is provided by the user.
#  Sum  the fir nnatural number
 #  SumFirstNaturalNumber.py

def main():
    print("Start")
    print("This program finds the sum of the first n natural numbers.")
    print()
 
    enter_number =int(input("Enter a Natural Number: "))
    sum = 0
    cont = 0
    for i in range(1, enter_number + 1):
      
    # cont = i 
        sum = sum + i
    # print(cont)
    print(f"The Sum from first to  {enter_number} is: {sum}")
    print("End")    

main()    
    