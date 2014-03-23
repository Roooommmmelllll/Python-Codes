# Arithmetic: +, -, *, /
# If/else, loops
# ask which problem types
# loop until entered Q
# repeat problem until they answer right

import random

def math_Add():
   num1 = random.randint(1,9)
   num2 = random.randint(1,9)
   correctAnswer = num1+num2
   loop = 1
   while (loop == 1):
      print("What is", num1, "+", num2, "?")
      guess = int(input())
      if (guess == correctAnswer):
         print("Correct!")
         break
      else:
         print("That is incorrect.")

def math_Subt():
   loop = 1
   while(loop == 1):
      num1 = random.randint(1,9)
      num2 = random.randint(1,9)
      correctAnswer = num1-num2
      if(correctAnswer >= 0):
         break
   while (loop == 1):
      print("What is", num1, "-", num2, "?")
      guess = int(input())
      if (guess == correctAnswer):
         print("Correct!")
         break
      else:
         print("That is incorrect.")

def math_Mult():
   num1 = random.randint(1,9)
   num2 = random.randint(1,9)
   correctAnswer = num1*num2
   loop = 1
   while (loop == 1):
      print("What is", num1, "*", num2, "?")
      guess = int(input())
      if (guess == correctAnswer):
         print("Correct!")
         break
      else:
         print("That is incorrect.")

def math_Div():
   loop = 1
   while(loop == 1):
      num1 = random.randint(1,9)
      num2 = random.randint(1,9)
      correctAnswer = num1/num2
      if(num1%num2 == 0):
         break
   while (loop == 1):
      print("What is", num1, "/", num2, "?")
      guess = int(input())
      if (guess == correctAnswer):
         print("Correct!")
         break
      else:
         print("That is incorrect.")

def main():
   loop = 1
   while (loop == 1):
      print("What type of math to practice: +, -, *, /")
      user = input("Or input Q to exit.")
      if(user == "+"):
         math_Add()
      elif(user == "-"):
         math_Subt()
      elif(user == "*"):
         math_Mult()
      elif(user == "/"):
         math_Div()
      elif(user == "Q"):
         break
main()
