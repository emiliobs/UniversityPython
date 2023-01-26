# A prgram to convert a textual message into a sequence of numbers, utilizing   the underlying Unicode encoding:

def main():
    print("This progrman convert a textual message into a sequyence")
    print("of number representating the unicode encoding of the message.\n")

    # get the messge to encode
    message = input("Please enter the message to encode: ")

    print("\nHere are  the unicode code: ")

    # Loop through the message and print out the unicode values for ch in message
    for ch in message:
        print(ord(ch), end= "")

    print()# blank line before prompt


main()      
    