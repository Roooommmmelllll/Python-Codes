#The sample file called studentdata.txt contains one line for
#each student in an imaginary class. The student's name is
#the first thing on each line, followed by some exam scores.
#The number of scores might be different for each student

#Using the text file studentdata.txt write a program that
#calculates the average grade for each student, and print
#out the student's name along with their average grade.

#Output the results to a data file titled "results1.txt"
#Your name and the date must be at the top of the data file.

#Think about whether you should read the data in line by line.

def checkLength(line):
   if len(line) > 8:
      return 1
   else:
      return 0

def checkZ(line):
   if line[0] == "z" or line[0] == "Z":
      return 1
   else:
      return 0

def checkPal(line):
   line = line[0:len(line)-1]
   reverse = line[::-1]
   if str(reverse) == str(line):
      return True
   else:
      return False
   
def problem2():
   readFile = open("allwords.txt", "r")
   outFile = open("results3.txt", "w")
   longWords = 0
   numberZs = 0
   palList = []
   
   for line in readFile:
      longWords = longWords + checkLength(line)
      numberZs = numberZs + checkZ(line)
      if checkPal(line) == True:
         palindrome = line[0:len(line)-1]
         palList.append(palindrome)
      
   toWrite = "Rommel Niduaza\nApril 10, 2014\n\n"
   toWrite += "Number of words longer than 8 letters: "
   toWrite += str(longWords)+"\n\n"
   toWrite += "Number of words starting with the letter 'Z': "
   toWrite += str(numberZs)+"\n\n"
   toWrite += "List of words that are palindromes:\n"

   outFile.write(toWrite)
   
   print(palList)

   for i in range(len(palList)):
      outFile.write(str(palList[i])+"\n")
   outFile.close()
   readFile.close()

def problem1():
   studentFile = open("studentdata.txt", "r")
   resultFile = open("results1.txt", "w")

   nameList = []
   averageList = []
   for line in studentFile:
      tempList = []
      tempList = line.split()
      nameList.append(tempList[0])
      total = 0
      average = 0
      for i in range(1,len(tempList)):
         total+=int(tempList[i])
      average = total/(len(tempList)-1)
      averageList.append(average)

   resultFile.write("Rommel Niduaza\n")
   resultFile.write("April 10, 2014\n")

   for i in range(len(nameList)):
      printLine = str(nameList[i]) + "\t" + str(averageList[i]) + "\n"
      resultFile.write(printLine)
      print(printLine)

   resultFile.close()
   studentFile.close()
 
def main():
   problem2()

main()
