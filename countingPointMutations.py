def getString():
   print("Please input a string of DNA.")
   print("The DNA string must only consist of the letters: G, A, T, and C.")
   print("Please keep both strings at equal length\n")
   newString = input()
   return newString

def checkContent(currentString):
   for i in range(len(currentString)):
      if (currentString[i] != 'G'):
         if (currentString[i] != 'A'):
            if (currentString[i] != 'T'):
               if (currentString[i] != 'C'):
                  print("The string must consist of only the letters: G, A, T, and C.")
                  print("Please input another string./n")
                  return False
   return True

def hamming(s, t):
   hammingDistance = 0
   for i in range(len(s)):
      if (s[i] != t[i]):
         hammingDistance += 1
   return hammingDistance

def main():
   contentS = False
   contentT = False
   
   while(contentS == False):
      s = getString()
      contentS = checkContent(s)
   print("\nEntry accepted.\n")

   t = getString()
   contentT = checkContent(t)
   
   while (len(s) != len(t) or contentT == False):
      if(contentT == False):
         t = getString()
         contentT = checkContent(t)
      if(len(s) != len(t)):
         print("The second string is of unequal length compared to the first.")
         print("The first string is", len(s), "long.")
         print("Please enter another string\n")
         t = getString()
         
   hammingDistance = hamming(s, t)

   print("There are", hammingDistance, "characters different between the two strings.")

main()

   
