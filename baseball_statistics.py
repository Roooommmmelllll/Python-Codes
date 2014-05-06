def addPlayer(names, jersey, team, position):
   newName = input("Please enter a player name:")
   names.append(newName)
   newJersey = input("Please enter that player's jersey number:")
   jersey.append(newJersey)
   newTeam = input("Please enter that player's team:")
   team.append(newTeam)
   newPosition = input("Please enter that player's position:")
   position.append(newPosition)
   return names, jersey, team, position

def allData(names, jersey, team, position):
   for i in range(0,len(names)):
      print("Player name: " + str(names[i]))
      print("Player jersey: " + str(jersey[i]))
      print("Player team: " + str(team[i]))
      print("Player position: " + str(position[i]) + "\n")

def teamData(names, jersey, team, position):
   teamList = []
   teamList.append(team[0])
   for x in range(1, len(team)):
      for v in range(0, len(teamList)):
         if (teamList[v] == team[x]):
            break
         else:
            teamList.append(team[x])
   print("There are these teams available:", teamList)
   teamName = input("Which team do you want to print?")
   for i in range(0,len(names)):
      if (teamName == team[i]):
         print("Player name: " + str(names[i]))
         print("Player jersey: " + str(jersey[i]))
         print("Player position: " + str(position[i]) + "\n")

def main():
   names = []
   jersey = []
   team = []
   position = []
   enterPlayer = 'y'
   while (enterPlayer == 'y'):
      names, jersey, team, position = addPlayer(names, jersey, team, position)
      enterPlayer = input("Would you like to enter another player?(Y)(N):").lower()

   teamData(names, jersey, team, position)

   print("\n\n----------ALL TEAM DATA----------\n\n")
   allData(names, jersey, team, position)

main()
