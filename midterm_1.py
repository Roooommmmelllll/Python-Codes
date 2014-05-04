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

   rawList = []
   for line in studentFile:
      rawList.append(line)

   arrayList = []
   for i in range(len(rawList)):
      arrayList[i] = rawList[i].split()
         
   nameList = []
   for i in range(len(arrayList)):
      nameList[i] = arrayList[0]

   averageList = []
   for i in range(len(averageList)):
      total = 0
      for j in range(1,len(arrayList)):
         total+=int(arrayList[j])
      average = total/(len(arrayList)-1)
      averageList[i] = average

   for i in range(len(nameList)):
      printLine = str(nameList[i]) + "\t" + str(averageList[i]) + "\n"
      resultFile.write(printLine)

   resultFile.close()
   studentFile.close()
