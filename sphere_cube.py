# Arithmetic: +, -, *, /
# If/else, loops
# ask which problem types
# loop until entered Q
# repeat problem until they answer right

import random

def sphereVol():
   r = int(input("Please enter the sphere's radius: "))
   volume = ((4/3)*3.14*r*r*r)
   print("The volume for that sphere is: ", volume)

def cubeVol():
   l = int(input("Please enter the cubes's length: "))
   w = int(input("Please enter the cubes's width: "))
   d = int(input("Please enter the cubes's depth: "))
   volume = (l*w*d)
   print("The volume for that cube is: ", volume)

def main():
   loop = 1
   while (loop == 1):
      print("Do you want to calculate volume for a sphere or cube?")
      user = input("(Input 'sphere' or 'cube') You can also input Q to quit.")
      if(user != "sphere" and user != "cube" and user != "Q"):
         print("That is not a valid input. Please input sphere or cube.")
      elif(user == "sphere"):
         sphereVol()
      elif(user == "cube"):
         cubeVol()
      elif(user == "Q"):
         break
      
main()
