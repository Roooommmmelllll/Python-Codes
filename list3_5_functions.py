def writeNums(FILE_NAME):
   file = open(FILE_NAME, "w")
   for i in range(3,100):
      if(i%3==0 or i%5==0):
         file.write(str(i)+"\n")
   file.close()

def readIntoList(FILE_NAME):
   file = open(FILE_NAME, "r")
   listOfNums = []
   for line in file:
      listOfNums.append(int(line))
   file.close()
   return listOfNums

def show5perLine(listOfNums):
   counter = 0
   for items in listOfNums:
      print(items, end="\t")
      counter += 1
      if (counter >= 5):
         print()
         counter = 0
   print("\n")

def minMaxAvgSum(listOfNums):
   minimum = 100
   maximum = 0
   total = 0
   for nums in listOfNums:
      if (nums > maximum):
         maximum = nums
      if (nums < minimum):
         minimum = nums
      total += nums
   avg = total/len(listOfNums)
   print("Minimum value is:", minimum)
   print("Maximum value is:", maximum)
   print("Sum of values is:", total)
   print("Average of values is:", avg)

def main():
   FILE_NAME = "multiplesOf3or5.txt"
   writeNums(FILE_NAME)
   listOfNums = readIntoList(FILE_NAME)
   show5perLine(listOfNums)
   minMaxAvgSum(listOfNums)

main()
