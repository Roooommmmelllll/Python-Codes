#In a weighted alphabet, every symbol is
#assigned a positive real number called a weight.
#A string formed from a weighted alphabet is
#called a weighted string, and its weight is
#equal to the sum of the weights of its symbols.
#The standard weight assigned to each number of
#the 20-symbol amino acid alphabet is the
#monoisotopic mass of the corresponding amino acid

#Given: A protein string P of length at most 1000 aa.
#Return: The total weight of P.
#Consult the monoisotopic mass table
#Hint: Put the above in a dicitonary
#Ask the user for a string
#Use a for loop to go through the string
#Use the string characters as the dicitonary keys.
#Add up all the values of the dictionary
#entries with matching keys.

def printLetters():
   letters = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L",
              "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"]
   print ("The letters available are:")
   count = 5
   for i in range(len(letters)):
      if count > 1:
         print(str(letters[i])+",", end=" ")
         count -= 1
      else:
         print(str(letters[i])+",", end=" ")
         count = 5
         print()

def main():
   massTableDictionary = {"A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259,
                "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406,
                "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293,
                "P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203,
                "T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333}
   printLetters()
   check = True
   while check == True:
      userString = input("Please input a string using the letters available(USE ALL CAPS):")
      total = 0
      for i in range(len(userString)):
         try:
            total+= massTableDictionary[userString[i]]
            check = False
         except:
            print("Error. String is invalid")
      print("The total string value for that string is:", total)

main()
