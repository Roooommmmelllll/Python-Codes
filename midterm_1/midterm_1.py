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

def main():
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

main()
