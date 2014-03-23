# Computer Assisted Instruction. Practice Arithmetic.
# At least 6 functions.
# Use echo printing where apporpriate (printing with variables)

# Extensions

# F) Extend your program so that it has differnt grade levels.
# For example, the program will only give problems with numbers at the level.
# Grade 1 - Numbers 1 > 5
# Grade 2 - Numbers 1 > 10
# Grade 3 - Numbers 1 > 20
# Using the score of how the student is doing overall, you can promote
# the student to the next grade level automatically if they are getting
# 90% or more right at their grade level.

import random

# A) Extend your program so that when the user gets the right answer,
# your program uses the random number generator to print out 1 out of
# 4 different possible responses.
# Do the same thing for their incorrect answers.
def randOutput(isCorrect):
   randNum = random.randint(1,4)
   if (isCorrect == True):
      if(randNum == 1):
         print("That is Correct!")
      elif(randNum == 2):
         print("Awesome, right answer!")
      elif(randNum == 3):
         print("Good Job! That was correct!")
      elif(randNum == 4):
         print("Amazing! That's right!")
   else:
      if(randNum == 1):
         print("I'm sorry, but that is incorrect.")
      elif(randNum == 2):
         print("Good try! But that is wrong :(")
      elif(randNum == 3):
         print("Sorry, that's the wrong answer.")
      elif(randNum == 4):
         print("That answer's a little off. Sorry.")

# C) Extend the program so that it evaluates the user by their scores.
# This will take place at the end of each math type.
# 100% right out of 10 problems, Amazing!
# 90% right out of 10 problems, Excellent!
# 80% is pretty good.
# 70 - 80% is average, but needs more practice.
# Below 70%, need a lot of review and practice.
# If they get below 70% the program will display  a review of that operation.
# For example, multiplication should show a multiplication table
def evaluateScore(percentCorrect):
   print("You got", percentCorrect, "% questions correct out of 10.")
   if(percentCorrect >= 90):
      print("Amazing job, you really have a knack for this!")
   elif(percentCorrect >= 80 and percentCorrect < 90):
      print("You should be proud of yourself!")
   elif(percentCorrect >= 70 and percentCorrect < 80):
      print("Almost there, a little more effort!")
   elif(percentCorrect < 70):
      print("You need some review and practice, here's some help.")

def extraHelp(operand):
   if(operand == "+"):
      print("\n\nRemember that addition is like adding two bags of things together.")
      print("If you have one bag of marbles, with 3 marbles in it.")
      print("And you have another bag of marbles, with 2 marbles in it.")
      print("Then you put all the marbles from one bag and put it into the other,")
      print("you can count the marbles one by one, from the other bag.")
      print("Right now, the second bag has 2 marbles, so take one out.")
      print("The first bag has 4 marbles in it now, and the second bag has only 1.")
      print("Then you can take the last marble out of the second bag.")
      print("The first bag now has 5 marbles in it, and the second bag is empty!")
      print("This idea works for anything, and in normal math looks like 3 + 2 = ?")
      print("Which is 5!\n\n")
   elif(operand == "-"):
      print("\n\nRemember that you can think of subtraction as taking marbles out of a bag.")
      print("If you have a bag of 3 marbles, and you wish to take 2 out.")
      print("You remove one marble, so the bag now has 2 marbles in it.")
      print("Then you remove another marble, so that the bag now has 1 marble in it.")
      print("You can think of this problem in normal math as, 3 - 2 = ?")
      print("Which equals 1!\n\n")
   elif(operand == "*"):
      print("/n/n")
      colLine = ""+str("%5.0f"%())
      for cols in range(1,13):
         colLine+= str("%5.0f"%(cols))
      print(colLine)
      for vert in range(1,13):
         line = ""+str(vert)
         for horiz in range(1,13):
            line += str("%5.0f"%(vert*horiz))
            print(line)
      print("/n/n")
   elif(operand == "/"):
      print("/n/nDivision is hard, but you cank think of it like this:")
      print("10 / 2 = ?")
      print("You subtract 2 from 10, until it reaches 0.")
      print("Then you add up how many times you had to subtract.")
      print("In this case, 10-2 = 8. 8-2 = 6. 6-2 = 4. 4-2 = 2. 2-2 = 0.")
      print("So, I had to subtract the 2 a total of five ( 5 ) times.")
      print("That means that 10 / 2 = 5!/n/n")
      
# Give the student 10 problems, using random numbers from 1 to 12.
# Questions should be in format, "What is 6 x 5?" or "What is 2 + 12?"
def mathAdd():
   counter = 0
   correct = 0
   while(counter < 10):
      tries = 0
      num1 = random.randint(1,12)
      num2 = random.randint(1,12)
      answer = num1+num2

      # D) Extend the program so that if the student gets it wrong, they can
      # try again and again until they get it right, and but is not counted
      # in their total for correct answers, it will only count by getting
      # it right on the first try.
      while(tries >= 0):
         print()
         print("What is", num1, "+", str(num2)+"?")
         user = input()

         # After giving an answer, check if the answer is correct, print out something like "Excellent!"
         if(int(user) == int(answer)):
            randOutput(True)
            if(tries == 0):
               correct += 1
               break
            else:
               break
         else:
            randOutput(False)
            tries+=1
         # If the answer is wrong, print out "Sorry, that is wrong. The correct answer is ##"
      counter += 1
      # Your program should keep a count of how many questions the
      # student gets right. And should let them know at the end what
      # percentage of the ten programs they got right. This should
      # display at the end of each practice session operation.
   percentCorrect = correct*10
   evaluateScore(percentCorrect)
   if(correct < 7):
      extraHelp("+")
   return correct
   
#def mathSub():

#def mathMult():

#def mathDiv():

# B) Extend the program by adding a Mixture option.
# Where they are given 10 questions using different Mathematics options.
#def mathMix():
   

# Present students with a menu, where they can repeatedly choose to practice.
# - Addition, Subtraction, Multiplication, and Division problems or to exit the program.
# User chooses math operation to practice ( +, -, *, / )
def main():
   totalCorrect = 0
   totalQuestions = 0
   while (totalQuestions >= 0):
      print("Please choose an operation to practice ( +, -, *, / )")
      print("You can enter M for a mix, or enter 0 (zero) to exit the program.")
      choice = input()
      if(choice == "0"):
         print("Thank you for using the Math Computer Assisted Instruction Program.")
         return
      elif(choice == "+"):
         numCorrect = mathAdd()
         # Keep track of a running score of the questions they got right in the whole program.
         # At the end of each 10 questions, the program should tell them their overall progress.
         # And then return to the menu.
         totalCorrect += numCorrect
         totalQuestions += 10
         print("You currently have gotten", totalCorrect, "questions correct out of", totalQuestions)
      elif(choice == "-"):
         mathSub()
      elif(choice == "*"):
         mathMult()
      elif(choice == "/"):
         mathDiv()
      elif(choice == "M"):
         mathMix()
      #else:
main()
