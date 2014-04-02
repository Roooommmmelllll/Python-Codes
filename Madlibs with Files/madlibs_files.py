#Your task is to write a MadLib program.
#A Madlib is a word game where a story has had certain
#elements removed and the program fills in the noun,
#color adjectives as appropriate.

#Example: Horses are leafy; violets are blue.

#Program must have at least three things that are read from
#data files.(noun, adjective, color)

import random

def howMany():
   print("How many madlibs do you want to use?")
   print("(Enter 0 (zero) to exit the program.")
   number = int(input())
   return number

def getNoun(nounList):
   randNum = random.randint(0,len(nounList)-1)
   return nounList[randNum]

def getColor(colorList):
   randNum = random.randint(0,len(colorList)-1)
   return colorList[randNum]

def getAdjective(adjectiveList):
   randNum = random.randint(0,len(adjectiveList)-1)
   return adjectiveList[randNum]

def main():
   print("Welcome to the Madlibs program.\n"+
         "This program will create random MadLibs to add to a file.\n"+
         "All you need to do is input how many words to use.")

   nounList = []
   colorList = []
   adjectiveList = []

   nounFile = open("nouns.txt", "r")
   colorFile = open("colors.txt", "r")
   adjectiveFile = open("adjectives.txt", "r")
   outputFile = open("output.txt", "w")

   for line in nounFile:
      nounList.append(line)
      
   for line in colorFile:
      colorList.append(line)
      
   for line in adjectiveFile:
      adjectiveList.append(line)

   nounFile.close()
   colorFile.close()
   adjectiveFile.close()

   loop = 1
   while (loop == 1):
      number = howMany()
      if number == 0:
         outputFile.close()
         break
      elif number == 1 or number == 2:
         print("That is not enough madlibs to make a sentence!")
      else:
         if (number == 3):
            rand = random.randint(1,2)
            if (rand == 1):
               madLib = "There once was a "+(getColor(colorList).replace('\n',''))+" "+(getNoun(nounList).replace('\n',''))+" who lived in a "+(getAdjective(adjectiveList).replace('\n',''))+" house."
            elif (rand == 2):
               madLib = "Some "+(getAdjective(adjectiveList).replace('\n',''))+" nights, you can hear the "+(getColor(colorList).replace('\n',''))+" "+(getNoun(nounList).replace('\n',''))+" howling.."
         elif (number == 4):
            rand = random.randint(1,1)
            if (rand == 1):
               madLib = "In the land of "+(getNoun(nounList).replace('\n',''))+", "+(getAdjective(adjectiveList).replace('\n',''))+" "+(getNoun(nounList).replace('\n',''))+"s were suddenly turning "+(getColor(colorList).replace('\n',''))+"!"
         outputFile.write(madLib+"\n")
         print(madLib)

   outputFile.close()
