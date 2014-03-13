def makeList():
   numbs = []
   for i in range(5):
      loop = True
      while loop == True:
         number = input("Enter an integer: ")
         if len(number) == 0:
            print("Please input a number!")
         else:
            if number[0] == " ":
               print("There's a space in the beginning, derrr")
            if number[0] == "-":
               if (number[1:len(number)]).isdigit() == True:
                  number = int(number)
                  numbs.append(number)
                  break
               else:
                  print("That is not an integer.")
            elif number.isdigit() == True:
               number = int(number)
               numbs.append(number)
               break
            else:
               print("That is not an integer.")
   print(numbs)

makeList()
