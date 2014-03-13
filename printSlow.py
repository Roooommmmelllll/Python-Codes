import time

def printSlow():
   print("Please input a speed to print at")
   print("0.5 is pretty fast, while 5 is very very slow.")
   printSpeed = float(input())
   newString = input("Input a long string: ")
   for i in range(len(newString)):
      print(newString[i], end="")
      time.sleep(printSpeed)

printSlow()
