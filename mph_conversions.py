def mphconvert():
    mph = float(input("Please input a speed in miles per hour to convert: "))
    #furlongs per fortnight conversion
    #1 mile = 8 furlongs
    #1 fortnight = 14 days
    #14 days = 336 hours

    #barleycorns per day conversion
    #1 mile = 5280 feet
    #1 foot = 36 barleycorns
    #1 day = 24 hours

    furlongsPerFortnight = float(mph * (8/336))
    barleycornsPerDay = float(mph * (190080/24))
    machNumber = float(mph/768.6)
    percentSpeedOfLight = float(mph/670616629*100)
    print(str(mph) + " miles per hour is equivalent to:\n" +
          str(furlongsPerFortnight) + " Furlongs Per Fortnight.\n" +
          str(barleycornsPerDay) + " Barleycorns Per Day.\n" +
          "Has a Mach Number of " + str(machNumber) +
          "\nand is " + str(percentSpeedOfLight) + "% of the Speed of Light.")

mphconvert()
