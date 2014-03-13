def whileLoops():
   oddcounter = 0
   evencounter = 0
   repeat = 0
   
   while repeat == 0:
      numum = int(input("Please input a number. Enter 0 (zero) to stop."))
      if  numum == 0:
         break
      elif numum%2 != 0:
         oddcounter += 1
      elif numum%2 == 0:
         evencounter +=1
      else:
         print("Invalid input")

   print ("You printed", evencounter, "even numbers, and", oddcounter, "odd numbers.")

whileLoops()
