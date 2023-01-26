# number2text2.py
# A program to convert a sequence of Unicode number into a string of text. Effiecinte version using a list accumulator.

def main():
    
    print("This program converts a sequence of Unicode numbers into")
    print("thge string of text that it represnet.\n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    #Loop throught each substring and build Unicode message
    chars = []
    for numStr in inString.split():
        codeNum = int(numStr)  # convert digits to a number
        chars.append(chr(codeNum)) # acculate new charater

    message = "".join(chars)
    print(f"\The decoded message is: {message}")




main()  