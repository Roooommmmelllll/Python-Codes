def hailstone(n, s):
   if (n%2 == 0):
      newN = n/2;
      s+=", "+str(int(newN))
      return newN, s
   else:
      newN = ((n*3)+1);
      s+=", "+str(int(newN))
      return newN, s

def addingFunction():
   loop = 1
   number = 0
   counter = 0
   while (loop == 1):
      userInput = int(input("Please enter a number: "))
      if(userInput <= 0):
         break
      else:
         counter+=1
         print(userInput, "+", number, "=", number+userInput)
         number = number+userInput
   print("You have run this function", counter, "times, with a total of", number)

def main():
##   n = int(input("Please enter a number for the hailstone sequence: "))
##   s = str(n)
##   while(n != 1):
##      n, s = hailstone(n, s)
##      if(n==1):
##         break
##   print(s)
   addingFunction()
   
main()
