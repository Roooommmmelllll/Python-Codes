def divide():

    topnum = int(input("Please input a number for the numerator:  "))
    botnum = int(input("Please input a number for the denominator:  "))

    if(botnum == 0):
        print("You cannot divide with zero!!")
        answer = "undefined"
        return
    
    answer = topnum/botnum

    print("The answer is " + str(answer) + ".")

def wages():
    hours = int(input("Please input the amount of hours that you worked:  "))
    wage = float(input("Please input your hourly wage:  "))

    if(hours < 0 or wage < 0):
        print("You cannot enter a negative number!!")
        return
    
    earnings = hours*wage

    print("You earned " + str(("%.2f")%earnings) + " dollars in " + str(hours) + " hours.")

def showMessage():
    message = "Hello, world!"
    answer = input("Do you want to see the message? (Y / N):  ")
    answer = answer.lower()

    if (answer == "yes" or answer == "y"):
        print(message)

def channel():
    print("This program will tell you what kind\nof programming is on the channel you enter.")
    channelNum = int(input("Please enter a favorite t.v. channel:  "))

    if (channelNum == 25):
        print("You must like sports.")
    if (channelNum == 72):
        print("You must like cartoons.")
    if (channelNum == 9):
        print("You must like public tv.")
    if (channelNum != 25 and channelNum != 72 and channelNum != 9):
        print("I do not know that channel.. :(")

def drive():
    print("This program will find out if you can drive a car in CA")
    age = int(input("How old are you?:  "))
    if (age >= 16):
        hasCar = input("Do you have a car? (Y/N):  ")
        hasCar = hasCar.lower()
        if (hasCar == 'y' or hasCar == 'yes'):
            hasLicense = input("Do you have a driver's license? (Y/N):  ")
            hasLicense = hasLicense.lower()
            if (hasLicense == 'y' or hasLicense == 'yes'):
                print("You can drive a car!")
            else:
                print("You need to have a car in order to drive..")
        else:
            print("You must have a license in order to drive a car.")
    else:
        print("You are not old enough to drive.")

drive()
