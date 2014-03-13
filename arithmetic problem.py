import random

def practice():
   valid = True
   while valid == True:
      choice = input("What kind of arithmetic do you wish to practice?")
      if choice == "+":
         loop1 = False
         while loop1 == False:
            ran1 = int(random.randint(0,9))
            ran2 = int(random.randint(0,9))
            check = ran1+ran2
            answer = 0
            again = True
            while again == True:
               print(ran1, "+", ran2, "= ?")
               answer = input("Enter your answer! Or enter 'Q' to exit the program!")
               if answer == "Q":
                  break
               answer = int(answer)
               if answer == check:
                  print("That is correct!")
                  break
               else:
                  print("That is incorrect. Please try again.")
            if answer == "Q":
               break
         if answer == "Q":
            break
         
      elif choice == "-":
         wrong = False
         while wrong == False:
            ran1 = int(random.randint(0,9))
            ran2 = int(random.randint(0,9))
            check = ran1-ran2
            answer = 0
            again = True
            while again == True:
               print(ran1, "-", ran2, "= ?")
               answer = input("Enter your answer! Or enter 'Q' to exit the program!")
               if answer == "Q":
                  break
               answer = int(answer)
               if answer == check:
                  print("That is correct!")
                  break
               else:
                  print("That is incorrect. Please try again.")
            if answer == "Q":
               break
         if answer == "Q":
            break
         
      elif choice == "*":
         wrong = False
         while wrong == False:
            ran1 = int(random.randint(0,9))
            ran2 = int(random.randint(0,9))
            check = ran1*ran2
            answer = 0
            again = True
            while again == True:
               print(ran1, "*", ran2, "= ?")
               answer = input("Enter your answer! Or enter 'Q' to exit the program!")
               if answer == "Q":
                  break
               answer = int(answer)
               if answer == check:
                  print("That is correct!")
                  break
               else:
                  print("That is incorrect. Please try again.")
            if answer == "Q":
               break
         if answer == "Q":
            break
      
      elif choice == "/":
         wrong = False
         while wrong == False:
            checkDivide = 1
            while checkDivide != 0:
               ran1 = int(random.randint(0,9))
               ran2 = int(random.randint(1,9))
               checkDivide = ran1%ran2
            check = ran1/ran2
            answer = 0
            again = True
            while again == True:
               print(ran1, "/", ran2, "= ?")
               answer = input("Enter your answer! Or enter 'Q' to exit the program!")
               if answer == "Q":
                  break
               answer = int(answer)
               if answer == check:
                  print("That is correct!")
                  break
               else:
                  print("That is incorrect. Please try again.")
            if answer == "Q":
               break
         if answer == "Q":
            break

      else:
         print("That is an invalid input. Try again.")
practice()
