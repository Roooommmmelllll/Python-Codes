def enterValue(students,midterm,final):
   
   print("Please enter values for the 6 students:")

   for i in range(6):
      students.append(input("Student's Name: "))
      midterm.append(int(input("Student's Midterm Percent Grade: ")))
      final.append(int(input("Student's Final Percent Grade: ")))

def doMath(midterm,final):

   grades = []
   curve = (midterm[0]+final[0])/2
   
   for i in range(6):
      avg = (midterm[i]+final[i])/2
      if avg > curve:
         curve = avg

   for i in range(6):
      avg = (midterm[i]+final[i])/2
      if avg > curve*.90:
         grades.append("A")
      elif avg >= curve*.80 and avg < curve*.90:
         grades.append("B")
      elif avg >= curve*.70 and avg < curve*.80:
         grades.append("C")
      elif avg >= curve*.60 and avg < curve*.70:
         grades.append("D")
      elif avg < curve*.60:
         grades.append("F")

   return grades   

def printMe(students,midterm,final,grades):

   for i in range(6):
      print(students[i],":",midterm[i],"on the midterm.",
            final[i],"on the final.","Grade:",grades[i])

def main():

   students = []
   midterm = []
   final = []

   enterValue(students,midterm,final)
   grades = doMath(midterm,final)
   printMe(students,midterm,final,grades)
   
main()
