#write a program that accepts positive integers from the user
#and tells how many of the numbers entered were odd and how many were even
#the program will stop asking for integers when the user inputs a zero

def countNumbers():
   odds = 0
   evens = 0
   newNum = -1

   while newNum != 0:
      newNum = input("Please input an integer: ")
      if newNum.isdigit() == False:
         print("You have not entered a nuber, please try again.")
      else:
         newNum = int(newNum)
         if newNum == 0:
            break
         elif newNum%2 == 0:
            evens+=1
         else:
            odds+=1

   print("You have entered", evens, "even numbers and", odds, "odd numbers.")

countNumbers()
