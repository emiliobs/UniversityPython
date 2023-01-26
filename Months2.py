# month2.py
# A program  to print the mont abbrevation, give its number

from calendar import month


def main():
    # month is a list used as a lookup table
    months =  ["Jan","Feb","Mar","Apr","May","Jun","jul","Aug","Sep","Oct","Nov","Dec"]

    n = int(input("Enter a month number (1 - 12): "))

    print(f"The month abbrevation is  {months[n-1]}")


main()