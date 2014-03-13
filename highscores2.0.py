##user enters the number of students
##and then enters each student's score on a test
##Output shows the 2 highest scores

def highest2Scores():
   #placeholders for highscores
   highscore1 = 0
   highscore2 = 0
   
   #placeholder for the number of students
   numStudents = int(input("How many students are there?: "))

   #loops input question for each student
   for i in range(numStudents):
      newScore = int(input("What score did you get on the test?: "))
      if newScore > highscore1 or newScore == highscore1:
         highscore2 = highscore1
         highscore1 = newScore
      elif newScore > highscore2 and newScore < highscore1:
         highscore2 = newScore

   print("The two highest scores are", highscore1, "and", highscore2) 
highest2Scores()
