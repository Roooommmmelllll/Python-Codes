import random

def randomNumGuess():
   correct = 0
   repeat = True
   while repeat == True:
      unknown = random.randint(1,100)
      guessRepeat = True
      while guessRepeat == True:
         guess = input("Please guess a number from 1 to 100: ")
         if guess.isdigit() == False:
            print("That is not a number!")
         else:
            guess = int(guess)
            if guess < 1 or guess > 100:
               print("That value is incorrect! Please try again!")
            elif guess < unknown:
               print("You are guessing too low, try again!")
            elif guess > unknown:
               print("You are guessing too high, try again!")
            elif guess == unknown:
               print("You are correct!")
               correct += 1
               break
            else:
               print("I wish I knew what to tell you, but it's broken...")
      again = input("Would you like to play again!")
      if again == "yes" or again == "y":
         print("Okay! Let's play again!")
      elif again == "no" or again == "n":
         print("You have won", correct, "times!")
         break
      else:
         print("What? Repeat?? OK!!!")
randomNumGuess()
