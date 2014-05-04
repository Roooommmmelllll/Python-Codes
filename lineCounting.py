import itertools

def lineCounter():
   count = 100
   lineCount = 0

   while count > 0:
      print("X ", end = "")
      count -= 1
      lineCount += 1
      if (lineCount== 10):
         print()
         lineCount = 0

def numberOrder():
   ## GENERATE EMPTY LIST
   listNumbers = []
   
   ## LIST INPUT
   for i in range(1,7):
      print("Please enter number", i,":")
      number = int(input())
      listNumbers.append(number)
      
   ## FIND LARGEST NUMBER
   biggest = listNumbers[0]
   bigIndex = 0
   for i in range(1,6):
      if( listNumbers[i] > biggest ):
         biggest = listNumbers[i]
         bigIndex = i
         
   ## PUT LARGEST NUMBER TO THE RIGHT
   tempNum = listNumbers[5]
   listNumbers[5] = biggest
   listNumbers[bigIndex] = tempNum
   
   ## PRINT LIST
   print(listNumbers)

def smallest3Numbers():
   ## GENERATE EMPTY LIST
   listNumbers = []
   
   ## LIST INPUT
   for i in range(1,6):
      print("Please enter Grade", i,":")
      number = int(input())
      listNumbers.append(number)
      
   ## SORT LIST FROM SMALLEST TO LARGEST
   hasSwapped = True
   while hasSwapped:
      hasSwapped = False
      for i in range(0,4):
         if( listNumbers[i] > listNumbers[i+1] ):
            temp = listNumbers[i+1]
            listNumbers[i+1] = listNumbers[i]
            listNumbers[i] = temp
            hasSwapped = True
            break
   
   ## PRINT LIST
   print(listNumbers[0],listNumbers[1],listNumbers[2])

def listPerms():
   # ORIGINAL PERMUTATION LIST
   n = "1234567"
   
   # USER INPUTS PERMUTATION LIMITS
   r = int(input("How many numbers do you wish to permutate (1 to 7)"))

   # CHANGE LIST TO USER INPUT
   n = n[0:r]

   # CREATE PERMUTATION LIST
   perms = itertools.permutations(n, r)
   listPerms = list(perms)

   # PRINT PERMUTATION LIST
   for x in range(0, len(listPerms)):
      print(listPerms[x])

def main():
   listPerms()

main()
