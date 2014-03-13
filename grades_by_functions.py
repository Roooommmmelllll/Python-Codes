def getAverage(grade1, grade2, grade3):
   average = grade1+grade2+grade3
   average = average/3
   return average

def getGrade():
   loop = 1
   while loop == 1:
      grade = int(input("Please enter a grade from 0 - 100"))
      if grade < 0 or grade > 100:
         print("Error, that is incorrect, please enter a grade from 0 - 100")
      else:
         return grade

def main():
   grade1 = getGrade()
   grade2 = getGrade()
   grade3 = getGrade()
   average = getAverage(grade1, grade2, grade3)
   if(average >= 85):
      print("You pass the class!")
   else:
      print("You do not pass :(")

main()
