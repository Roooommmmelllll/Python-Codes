import random

def makeList():
   numList = []
   for i in range(50):
      numList.append(random.randint(0,100))
   return numList

def stats(numList):
   total = 0
   minimum = 100
   maximum = 0
   for i in range(50):
      total+=numList[i]
      if (numList[i] < minimum):
         minimum = numList[i]
      if (numList[i] > maximum):
         maximum = numList[i]
   average = total/50
   print("Average is:", average)
   print("Minimum is:", minimum)
   print("Maximum is:", maximum)

def bubbleSort(numList):
   swapped = True
   while(swapped == True):
      swapped = False
      for i in range(0,50):
         for j in range(i+1,50):
            if(numList[i] > numList[j]):
               temp = numList[i]
               numList[i] = numList[j]
               numList[j] = temp
               swapped = True
   return numList

def printList(numList):
   print(numList)

def main():
   numList = makeList()
   printList(numList)
   stats(numList)
   sortedList = bubbleSort(numList)
   printList(sortedList)

main()
