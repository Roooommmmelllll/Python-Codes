def getSides():
   print("Please enter the three sides for a triagnle.\n" +
         "Program will determine if it is a right triangle.")
   sideA = int(input("Side A: "))
   sideB = int(input("Side B: "))
   sideC = int(input("Side C: "))
   return sideA, sideB, sideC

def checkRight(sideA, sideB, sideC):
   if sideA >= sideB and sideA >= sideC:
      if sideA**2 == (sideB**2+sideC**2):
         return True
   elif sideB >= sideA and sideB >= sideC:
      if sideB**2 == (sideA**2+sideC**2):
         return True
   elif sideC >= sideA and sideC >= sideB:
      if sideC**2 == (sideA**2+sideB**2):
         return True
   return False

def printMe(right):
   if right == True:
      print("Those values create a right triangle!")
   else:
      print("Those values DO NOT create a right triangle!")
               
def main():
   sideA, sideB, sideC = getSides()
   #checkTriangle
   right = checkRight(sideA, sideB, sideC)
   printMe(right)
               
main()
