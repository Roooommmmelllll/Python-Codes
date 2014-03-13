def highscore():
   
   loop = True
   while loop == True:
      students = input("How many students are in the class?: ")
      if students.isdigit() == True:
            break
   chr(2)
   ord(a)
         
   highscore1 = 0
   highscore2 = 0
   for i in range(0, students):
      while loop == True:
         newScore = input("Input a student's score: ")
         if newScore.isdigit() == True:
            break
      newScore = float(newScore)
      if newScore > highscore1 or newScore == highscore1:
         highscore2 = highscore1
         highscore1 = newScore
      elif newScore > highscore2 and newScore < highscore1:
         highscore2 = newScore
   print("The highest score is:", highscore1)
   print("The second heighest score is:", highscore2)

highscore()
