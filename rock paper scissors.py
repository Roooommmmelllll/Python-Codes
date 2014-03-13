import random

def computer():
   cpu = random.randint(1,3)
   if cpu == 1:
      return "rock"
   elif cpu == 2:
      return "paper"
   elif cpu == 3:
      return "scissors"

def player():
   while True:
      you = input("Please choose!\nType in 1 for Rock\nType in 2 for Paper\nType in 3 for Scissors\n")
      if you.isdigit() == False:
         print("Error, try again.\n")
      else:
         you = int(you)
         if you == 1:
            return "rock"
         elif you == 2:
            return "paper"
         elif you == 3:
            return "scissors"
         else:
            print("Error, try again.\n")
      return you

def checkWin(cpu,you):
   if cpu == "rock" and you == "rock":
      print(cpu, "vs", you)
      print("You tied!")
      return 0
   elif cpu == "rock" and you == "paper":
      print(cpu, "vs", you)
      print("You win!")
      return 1
   elif cpu == "rock" and you == "scissors":
      print(cpu, "vs", you)
      print("You lose!")
      return 2
   elif cpu == "paper" and you == "rock":
      print(cpu, "vs", you)
      print("You lose!")
      return 2
   elif cpu == "paper" and you == "paper":
      print(cpu, "vs", you)
      print("You tied!")
      return 0
   elif cpu == "paper" and you == "scissors":
      print(cpu, "vs", you)
      print("You win!")
      return 1
   elif cpu == "scissors" and you == "rock":
      print(cpu, "vs", you)
      print("You win!")
      return 1
   elif cpu == "scissors" and you == "paper":
      print(cpu, "vs", you)
      print("You lose!")
      return 2
   elif cpu == "scissors" and you == "scissors":
      print(cpu, "vs", you)
      print("You tied!")
      return 0

def RPS():
   winCount = 0
   loseCount = 0
   tieCount = 0
   while True:
      cpu = computer()
      you = player()
      winner = checkWin(cpu, you)
      if winner == 0:
         tieCount += 1
      elif winner == 1:
         winCount += 1
      elif winner == 2:
         loseCount += 1
      again = input("Do you want to play again? (y or n): ")
      if again == "n":
         break
   print("You won", winCount, "times! But you tied", tieCount, "times and lost", loseCount ,"times.")
   print("Thanks for playing! Try again next time!")

RPS()
