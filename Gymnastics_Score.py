# Write a program to compute a gymnastics
# competition core. There are 4 judges who
# mark the gymnasts in the range of 0 to 10.
# The overall score is the average of the
# marks. An error message should appear if
# a mark is entered that is out of the range
# (0-10) Output the average. Format the
# output nicely, so it is easy to read and
# to follow.

def gymScore():
   total = 0
   repeat = 4
   while repeat > 0:
      score = int(input("Please input a score from 0 - 10:  "))
      if score < 0 or score > 10:
         print("Invalid Input. Please try again.")
      else:
         total += score
         repeat -= 1
   average = total / 4
   print("The gymnast has an average score of", "%.2f"%average)
gymScore()
