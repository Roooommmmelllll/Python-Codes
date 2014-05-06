import random

def makeList():
   numList = []
   for i in range(4):
      numList.append(random.randint(10,50))
   return numList

def bubbleSort(numList):
   swapped = True
   while(swapped == True):
      swapped = False
      for i in range(0,4):
         for j in range(i+1,4):
            if(numList[i] > numList[j]):
               temp = numList[i]
               numList[i] = numList[j]
               numList[j] = temp
               swapped = True
   return numList

def printList(numList):
   print(numList)

def sortedInsert(numList):
   num = int(input("Enter a number between 10 and 50"))
   for i in range(len(numList)):
      if (num <= numList[0]):
         numList.insert(0, num)
         return numList
      if (num > numList[i]):
         if (i == len(numList)-1):
            numList.append(num)
            return numList
         elif (num <= numList[i+1]):
            numList.insert(i+1, num)
            return numList

def main():
   numList = makeList()
   printList(numList)
   numList = bubbleSort(numList)
   printList(numList)
   
   numList = sortedInsert(numList)
   printList(numList)
   numList = sortedInsert(numList)
   printList(numList)

main()
