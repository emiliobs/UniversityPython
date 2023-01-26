#Exercise 12
#  Write a program to find the sum of the cubes of the first n natural numbers 
#  where the value of n is provided by the user.
  #SumOfTheCubes.py
   
def main():
    print("Start")
    print("This program finds the sum of the cubes of the first n natural numbers.")
    print()
 
    enter_number_cubes =int(input("Enter a Natural Number: "))
    
    sum = 0
    cont = 0
    for i in range(1, enter_number_cubes + 1):
    
        
      
      
    # cont = i 
        sum = sum + pow(i, 3)
        # print(cont)
    print(f"The Sum of the cubes from first to  {enter_number_cubes} is: {sum}")
    print("End")    

main()    