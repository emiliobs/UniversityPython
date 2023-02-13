
def happy():
  return "Happy Birthday to you!\n"

def verseFor(person): 
  lyrics = happy() *2 + "Happy birthday, dear " + person + ". \n" + happy() 
  return lyrics 


def main():
  outFile = open("HappyBirthday.txt", "w")
  for person in ["Emilio", "Lucas", "Camilo"]:
    print(verseFor(person), file= outFile)
  outFile.close() 
  
  
main()  
    