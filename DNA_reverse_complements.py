#in DNA strings, symbols A and T are complements of each other,
#as are C and G. Given a nucleotide p, we denote its complementary
#nucleotide as /p.

def main():
   readFile = open("startFile.txt", "r")
   string = "ATGTGACGTACAGT"
   newString = ""
   for i in range(len(string)):
      if (string[i] == "A"):
         newString += "T"
      elif (string[i] == "T"):
         newString += "A"
      elif (string[i] == "C"):
         newString += "G"
      elif (string[i] == "G"):
         newString += "C"

   newString = newString[::-1]
   print(string)
   print(newString)
   
main()
