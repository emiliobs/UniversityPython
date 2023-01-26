#EXERCISE 16
#A Fibonacci sequence is a sequence of numbers where each successive 
# number is the sum of the previous two. The classic Fibonacci sequence 
# begins: 1, 1, 2, 3, 5, 8, 13, .... Write a program that computes the nth 
# Fibonacci number where n is a value input by the user. For example, if 
# n = 6, then the result is 8.
 #fibonacciSequence.py
 
print("Start")


def main():
    print("This program find the Fibonacci dequence is of the numbers.")
    print()
    
    
    n_number = int(input("Enter the value of N?: "))
    curre, prev =1 , 1
    for i in range(n_number-2):
        curre, prev = curre + prev, curre
        print(curre)
    print()
    print()
    print()
    print(f"The Fibonacci number is: {curre}")
 
main()       