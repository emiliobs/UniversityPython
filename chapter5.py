# month.py
# A program to print ther abbrevation of a month, given its number

def main():
    #monthgs is used as a lookup table
    months = "JunFebMarAprMayJunJulAugJulSepOctNovDec"

    n = int(input("Enter a month number (1 - 12): "))

    # compute starting position  of month a in months

    pos = (n - 1) * 3

    # Grab the appropriate slice from months
    monthAbbrev = months[pos+3]

    #print the result
    print(f"The month abbrevation is {monthAbbrev} '.' ")

main()