def nameList():
   names = ["Mel Gibson", "Johnny Depp", "Gerard Butler", "Angelina Jolie", "Denzel Washington"]
   favorite = input("Name your favorite actor: ")
   length = len(names)
   for i in range(0, length):
      if favorite == names[i]:
         print("Yes, that's a famous actor.")
         break
   print("That actor isn't on the list!")
   
nameList()
   
