#how many rooms need to be reserved
#program asks how many is in the maximum number of peopelwho should be in each room
#assume that the same amount of poeple are maximum in each room
#each room must reserve the number of rooms required + 1

def convention():
    print("Welcome to the Salinas Convention Center!")
    people = int(input("How many people will be attending your event? "))
    rooming = int(input("How many people do you want to have in each of the rooms? "))
    answer = people/rooming
    room = int(answer) + 1
    if (answer%1 > 0):
        room = room+1

    print ("You will need " + str(room) + " rooms!")
convention()
