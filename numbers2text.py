# number2text.property
# A program to convert a sequence of unicode number into a string of text

def main():
    print("This program convert a sequence of Unicode numbers into the String of text that it represent.\n")

    # Get the message to ecode
    inString = input("Please enter the Unicode-encode message: ")

    message = ""
    # Loop through each subtring and build Unicode message
    for numStr in inString.split():
        codeNum = int(numStr) #convert digits  to a number
        message = message + chr(codeNum) # concatenate character to message
        print(f"\The decoded message is: {message}")

    print(f"\The decoded message is: {message}")


main()        