
def happy(): 
  return "Happy Birthday to you!\n"



def verseFor(person):
  lyrics = f"{happy() * 2} Happy birthday, dear {person} .\n {happy()}"
  return lyrics

def main():
  for person in ["Emilio","Camilo", "Lina"]:
    print(verseFor(person))
    
    
    
main()    
    