#create a function that prings a string parameter.
#the program will ask the user to input a string
#then it will send that value to the print function
#and it will print it out

def myPrint(stringParameter):
   print(stringParameter)

#stringParameter = input("Enter a string: ")
#myPrint(stringParameter)

#rock paper or scissors
#user will choose 1, 2 or 3
#functions will be called to print rock, paper, or scissors

def rock():
   print("Rock")
   
def paper():
   print("Paper")
   
def scissors():
   print("Scissors")

def main():   
   user = input("Input a number: (1 for Rock, 2 for Paper, 3 for Scissors)")
   if user == "1":
      rock()
   elif user == "2":
      paper()
   elif user == "3":
      scissors()
   else:
      print("That is not a choice")

main()
