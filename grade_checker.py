# Program to show a student's letter gade in a course
# based on their percentage grade
# 90+ gets an A, 80 - 89 gets a B, 70 - 79 gets a C,
# 60 - 69 gets a D, and 59- gets an F

def gradeCheck():
   percent = int(input("What percent grade do you have in the class?: "))

   if percent >= 90:
      print("You get an A!!")
   elif percent < 90 and percent >= 80:
      print("You get a B!")
   elif percent < 80 and percent >= 70:
      print("You get a C.")
   elif percent < 70 and percent >= 60:
      print("You get a D..")
   elif percent < 60:
      print("You get an F....")
      
gradeCheck()

