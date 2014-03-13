import random

def arithmeticSkill():
   answer = input("would you like to +,-,* or / ? ")

   while answer == "+":
      var1 = random.randint(0,9) # generates random numbers
      var2 = random.randint(0,9)

      total = 1
      while valid == False:

         print("What is", var1, "+", var2, "? enter 'Q' at any time to stop program")
         total = input()
   
         if total == 'Q':
            return()
         total= int(total)
         result = var1 + var2
         
         if total != result:
            print("wrong try again!")
         elif total == result:
            print("good job you got it right!")
            break

   while answer == "-":
      var1 = random.randint(0,9) # generates random numbers
      var2 = random.randint(0,9)

      total = 1
      while valid == False:

         print("What is", var1, "-", var2, "? enter 'Q' at any time to stop program")
         total = input()
   
         if total == 'Q':
            return()
         total= int(total)
         result = var1 - var2
         
         if total != result:
            print("wrong try again!")
         elif total == result:
            print("good job you got it right!")
            break

   while answer == "*":
      var1 = random.randint(0,9) # generates random numbers
      var2 = random.randint(0,9)

      total = 1
      while valid == False:

         print("What is", var1, "*", var2, "? enter 'Q' at any time to stop program")
         total = input()
   
         if total == 'Q':
            return()
         total= int(total)
         result = var1 * var2
         
         if total != result:
            print("wrong try again!")
         elif total == result:
            print("good job you got it right!")
            break

   while answer == "/":
      remainder = 1
      while remainder != 0:
         var1 = random.randint(0,9) # generates random numbers
         var2 = random.randint(1,9)
         remainder = var1%var2
      
      total = 1
      while valid == False:

         print("What is", var1, "/", var2, "? enter 'Q' at any time to stop program")
         total = input()
   
         if total == 'Q':
            return()
         total= int(total)
         result = var1 / var2
         
         if total != result:
            print("wrong try again!")
         elif total == result:
            print("good job you got it right!")
            break

arithmeticSkill()
