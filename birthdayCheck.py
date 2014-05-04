def checkLen(bday):
   if(len(bday) != 10):
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
      return False
   else:
      return True

def checkYear(year):
   age = -1*(year-2013)
   if (age > 123):
      return False
   elif (year >= 2013):
      return False
   else:
      return True

def checkDay(day, month, year):
   daysEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   if (year % 4 == 0):
      daysEachMonth[1] = 29
   if (day <= daysEachMonth[month-1]):
      return True
   else:
      return False
      
def main():
   birthday = input("Please enter your birthday:")
   bdayLen = checkLen(birthday)
   month, day, year = getData(birthday)
   bdayMon = checkMon(month)
   bdayYear = checkYear(year)
   bdayDay = checkDay(day, month, year)

main()
