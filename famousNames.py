
def famousNames():
   greekGods = ["Aphrodite", "Athena",  "Zeus", "Poseidon", "Hades", "Ares", "Hera", "Hercules", "Hephaestus"]   
   user = input("Please input the name of your favorite Greek God!\n")
   for i in range(len(greekGods)):
      if greekGods[i] == user:
         print("That is also one of my favorite Greek Gods!")
         break
      if i >= (len(greekGods)-1):
         print("Aww, I don't know that God, or that isn't a Greek God! or I don't like them.")
         break

famousNames()
