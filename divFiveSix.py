# Program will display al numbers from 100 to 1000
# All those numbers are divisible by 5 and 6
# All those numbers will be displayed ten numbers
# per line, and exactly one space between them.

def divFiveSix():
   count = 0
   for i in range(100,1001):
      if count >= 10:
         print()
         count = 0
      if i%5 == 0:
         print (i, end=' ')
         count += 1
      elif i%6 == 0:
         print (i, end=' ')
         count += 1
divFiveSix()
