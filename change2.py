# change2.py
# A program to calculate the value of some change in dollar this version represnet the total cash in cents.

def main():
    print("Change Counters\n")
    print("Please enter the count of each cash in cents.")
    quearters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))

    total = quearters * 25 + dimes * 10 + nickles * 5 + pennies

    print("The total value of your change is £{0}.£{1:0>3}".format(total // 100, total % 100))
    # print(f"The total value of your change is {total // 100:0}, {total % 100:1}")
   
main() 