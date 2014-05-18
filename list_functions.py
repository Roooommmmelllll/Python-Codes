import random

def norm(stringList):
   print(stringList)

def sortList(stringList, backwards):
   if(not backwards):
      stringList.sort()
   else:
      stringList.sort()
      stringList.reverse()
   print(stringList)

def rand(stringList):
   number = random.randint(1,10)
   
   while number > 0:
      swapNum = random.randint(0,4)
      swapPlace = swapNum
      
      while(swapPlace == swapNum):
         swapPlace = random.randint(0,4)
         
      temp = stringList[swapNum]
      stringList[swapNum] = stringList[swapPlace]
      stringList[swapPlace] = temp
      number -= 1
      
   print(stringList)

def main():
   stringList = []
   for i in range(5):
      stringList.append(input("Please input a string: "))
   print("Normal")
   norm(stringList)
   print("Alphabetical")
   sortList(stringList, False)
   print("Reverse Alphabetical")
   sortList(stringList, True)
   print("Random")
   rand(stringList)

main()
