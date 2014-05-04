def checkLen(bday):
   if(len(bday) != 10):
      print("You did not enter 8 numbers and two forward slashes.")
      return False
   else:
      return True
   
def getData(bday):
   bdayList = bday.split("/")
   month = int(bdayList[0])
   day = int(bdayList[1])
   year = int(bdayList[2])
   return month, day, year

def checkMon(month):
   if (month < 1 or month > 12):
      print("The month you entered needs to be a number between 1 - 12")
      return False
   else:
      return True

def checkYear(year):
   age = -1*(year-2013)
   if (age > 123):
      print("Nobody is that old! (Year is more than 123 years old.)")
      return False
   elif (year >= 2013):
      print("You entered a year in the future, or are zero years old! (year >= 2013)")
      return False
   else:
      return True

def checkDay(day, month, year):
   daysEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   namesEachMonth = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
   if (year % 4 == 0):
      daysEachMonth[1] = 29
   if (day <= daysEachMonth[month-1]):
      return True
   else:
      print("You did not enter the right number of days for that month!")
      print(namesEachMonth[month-1], "has", daysEachMonth[month-1], "in it!")
      return False
      
def main():
   print("Please enter your 8 digit birthday")
   birthday = input("in the following format: month/day/year: ")
   check = True
   while(check):
      check = checkLen(birthday)
      if (check == False):
         break
      
      month, day, year = getData(birthday)
      
      check = checkMon(month)
      if (check == False):
         break
      
      check = checkYear(year)
      if (check == False):
         break

      check = checkDay(day, month, year)
      if (check == False):
         break

      print("That is a valid birthday!")
      break

main()
