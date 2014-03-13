def rain():
   #nested loop, rainfall over a period
   #of years first program asks for the
   #number of years each loop asks for the
   #rainfall in a month in inches the end
   #of the program displays the number of
   #months, the total inches of rainfall
   #and the average rainfall per month for
   #the entire period.
   months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
   loop = True
   while loop:
      years = input("How many years of rainfall do you wish to keep track of?: ")
      if years.isdigit() == True:
         years = int(years)
         if years < 0:
            print("Invalid input, please try agian.")
         else:
            break
      else:
         print("Invalid input, please try again.")
   while loop:
      theYear = input("What year do you wish the program to start in?: ")
      if theYear.isdigit() == True:
         theYear = int(theYear)
         if theYear < 0:
            print("Invalid input, please try agian.")
         else:
            break
      else:
         print("Invalid input, please try again.")
   firstYear = theYear
   theYear -= 1
   totalRain = 0
   totalMonths = years*12
   while years > 0:
      monthCounter = 0
      theYear += 1
      while monthCounter < 12:
         print("For the month of", months[monthCounter], str(theYear) +
               ", rainfall measured at: ")
         currentRain = input()
         if currentRain.isdigit() == True:
            currentRain = int(currentRain)
            totalRain += currentRain
            monthCounter += 1
         else:
            print("Invalid input, please try again.")
      years -= 1
   averageRain = (totalRain/totalMonths)
   print("From", months[0], firstYear, "to", months[11], theYear,
         "over a period of", totalMonths, "the total rainfall of",
         totalRain, "has averaged out to:", str(averageRain), "inches per month!")
rain()
