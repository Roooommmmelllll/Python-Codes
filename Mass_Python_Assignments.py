def rotateList():
   rotate = []
   size = int(input("How many elements do you want in the list?: "))
   for i in range (1,size+1):
      rotate.append(int(input("Please enter element " + str(i) + ": ")))
   rotation = int(input("By how many elements do you wish to rotate the list? "))
   for i in range(rotation):
      temp = rotate[0]
      for x in range(len(rotate)-1):
         rotate[x] = rotate[x+1]
      rotate[size-1] = temp
   print (rotate)

def countClumps():
   numList = []
   size = int(input("How many values do you want in the list?: "))
   for i in range (1,size+1):
      numList.append(int(input("Please enter a value: ")))
   clumps = 0
   found = False
   for i in range(len(numList)-1):
      if(not found):
         if(i != len(numList)-1 and numList[i] == numList[i+1]):
            found = True
            clumps += 1
      else:
         if(i != len(numList)-1 and numList[i] != numList[i+1]):
            found = False
   print("The list has", clumps, "clumps in it.")
   
def allLess(L1, L2):
   check = True
   for x in L1:
      for y in L2:
         if (x > y):
            check = False
   return check

def checkAllLess():
   L1 = [1, 2, 3, 4, 5]
   L2 = [6, 7, 8, 9, 10]
   check = allLess(L1,L2)
   print("All values are less?: ", check)

def randPokemon():
   pokemon[]

def pokemon():
   active = "Pikachu"
   party = ["Charmeleon", "Geodude", "Gyrados", "Butterfree", "Mankey"]
   while(active != ""):
      
      for pokemon in party:
         print(pokemon,end="")
      print("\n\nEnter 0 to exit the program.")
      swap = int(input("Which pokemon do you want to swap " + str(active) + " with? (1-5):\n"))
      if(swap != 0):
         temp = party[swap-1]
         party[swap-1] = active
         active = temp
      else:
         break

pokemon()
