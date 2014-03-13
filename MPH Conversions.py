# 1 meter = 117.64 barleycorns
# 1 furlong = 220 yards
# 1 fortnight = 2 weeks
# 1 MACH = speed of sound
# The speed of sound = 1130
#     feet per second
# 1 PSL is a speed compared to the
#     speed of light.
# The speed of light is 299,792,458
#     meters per second
# 1 Foot = .3048 Meters

def convert():
   mph = int(input("Please input a speed in Miles Per Hour."))

   #1 meter = 117.64 barleycorns
   #1 foot = .3048 meters
   #1 mile = 5,280 feet
   #5,280 feet * .3048 = meters in a mile
   #5,280 feet * .3048 * 117.64 = barleycorns in a mile

   #1 day = 24 hours
   #hours * 24 = hours in terms of days
   
   barleyCornsPerDay = (mph * 5280 * .3048 * 117.64 / 24)

   #1 furlong = 220 yards
   #1 fortnight = 2 weeks
   #1 mile = 5,280 feet
   #5,280 feet / 3 = yards in a mile
   #5,280 feet / 3 / 220 = furlongs in a mile

   #1 day = 24 hours
   #1 week = 14 days
   #hours * 24 = hours in terms of days
   #hours * 24 * 14 = hours in terms of fortnights

   furlongsPerFortnight = (mph * 5280 / 3 / 220 / 24 / 14)

   #1 MACH = speed of sound
   #The speed of sound = 1130 feet per second
   #1 mile * 5,280 feet = miles in terms of feet
   #60 minutes in 1 hour
   #60 seconds in 1 minute
   #1 hour * 60 = 1 hour in terms of minutes
   #1 hour * 60 * 60 = 1 hour in terms of seconds

   SoS = (mph * 5280 / 60 / 60)
   machNumber = SoS / 1130

   #5,280 feet * .3048 = meters in a mile
   #60 minutes in 1 hour
   #60 seconds in 1 minute
   #1 hour * 60 = 1 hour in terms of minutes
   #1 hour * 60 * 60 = 1 hour in terms of seconds
   # The speed of light is 299,792,458 meters per second

   metersPerSecond = (mph * 5280 * .3048 / 60 / 60)
   percentSoL = metersPerSecond/299792458*100

   print(str(mph) + " Miles Per Hour is: ")
   print("In terms of Barleycorns Per Day: " + str(barleyCornsPerDay))
   print("In terms of Furlongs Per Fortnight: " + str(furlongsPerFortnight))
   print("Has a Mach Number of: " + str(machNumber))
   print("And has a Percent Speed of Light of: " + str(percentSoL))

convert()
