def woot():
   print("Program will determine the " +
         "fastest route between four " +
         "points of travel.")
   print("Assume that point A is already plotted")
   pointsNum = 0
   while pointsNum < 6:
      pointsNum+=1
      if pointsNum == 1:
         pointAB = int(input("Please input the distance" +
                               "from point A to B")
      elif pointsNum == 2:
         pointAC = int(input("Please input the distance" +
                               "from point A to C")
      elif pointsNum == 3:
         pointAD = int(input("Please input the distance" +
                               "from point A to D")
      elif pointsNum == 4:
         pointBC = int(input("Please input the distance" +
                               "from point B to C")
      elif pointsNum == 5:
         pointBD = int(input("Please input the distance" +
                               "from point B to D")
      elif pointsNum == 6:
         pointCD = int(input("Please input the distance" +
                               "from point C to D")
   check1 = pointAB + pointBC + pointCD
   shortest = check1
   check2 = pointAB + pointBD + pointCD
   if check1 > check2:
      shortest = check2
   else:
      
