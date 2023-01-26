#Exercise 15
# Write a program that approximates the value of pi by summing the terms 
# of this series: 4/1- 4/3 + 4/5- 4/7 + 4/9- 4/11 + ... The program should 
# prompt the user for n, the number of terms to sum, and then output the 
# sum of the first n terms of this series. Have your program subtract the 
# approximation from the value of math. pi to see how accurate it is.
 #valuepfpi.py
import math
print("Start")
def main():
    print("This program approximates the value of pi by summing a fixed")
    print("number of terms in a series.")
    print()   
    n_numbers = int(input("How many terms should I use? "))
    sum = 0.0
    for i in range(1, n_numbers + 1):
        n_serie = float(input("Enter number to Serie: ")) 
        #c_serie = 4 * pow(-1, n_serie + 1) / (2 * n_serie - 1)
        c_serie = 4 * ((-1)**(n_serie + 1 )) / (2 * n_serie - 1)
        print(c_serie)
        print()
        sum  = sum + c_serie      
    print(f"Approximation to pi is: {sum}")
    print(f"Difference from math.pi: {math.pi - sum}" )           
print("End")  
# total = 0.0   
# def main():
#     print("This program approximates the value of pi by summing a fixed")
#     print("number of terms in a series.")
#     print()
    
#     n = int(input("How many terms should I use? "))

#     total = 0.0
#     sgn = 1.0   # used to alternate sign of terms
#     for denom in range(1, 2*n, 2):
#         total = total + sgn * 4.0/denom
#         sgn = -sgn #flip the sign

#         print("Approximation to pi is:", total)
#         print("Difference from math.pi:", math.pi - total)     
                    
main() 
