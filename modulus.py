import random

def rooms():
    print("Room Reservation")
    people = 96
    roomSize = 30
    numRooms = int(people / roomSize)
    leftOvers = int(people % roomSize)
    print("You need", str(numRooms), "rooms.")
    print("There will be", str(leftOvers), "people left over.")

def oddEven():
    print("Odd or Even?")
    number = random.randint(-100,100)
    if number % 2 == 0:
        print(str(number), "is even.\n")
    else:
        print(str(number), "is odd.\n")

def tuition():
    year = 1
    cost = 10000
    percent = 1.05
    while year < 10:
        print("Year", year, cost)
        cost = cost*percent
        year +=1

tuition()
