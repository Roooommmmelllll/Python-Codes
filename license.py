def main():
    repeatM = 1
    while (repeatM == 1):
        print("This program will find out if you can drive a car in CA.")
        repeatM = drive()
        askRepeat = 1
        while (askRepeat == 1):
            ask = input("Try this program again? (Y/N) ")
            ask = ask.lower()
            if (ask == 'y' or ask == 'yes'):
                askRepeat = 0
            elif (ask == 'n' or ask == 'no'):
                print("Thank you for using Rom Can Drive. Have a nice day.")
                askRepeat = 0
                repeatM = 0
            else:
                print("Invalid input. Please use Y/N")
def drive():
    repeat = 1
    while (repeat == 1):
        age = int(input("How old are you?:  "))
        if (age < 0 or age > 110):
            print("Invalid age input. Try Again.")
        elif (age >= 16):
            repeat = 0
        else:
            print("You are not old enough to drive.")
            return 1

    repeat = 1
    while (repeat == 1):
        hasCar = input("Do you have a car? (Y/N):  ")
        hasCar = hasCar.lower()
        if (hasCar == 'y' or hasCar == 'yes'):
            repeat = 0
        elif (hasCar == 'n' or hasCar == 'no'):
            print("You must have a car... in order to drive a car.")
            return 1
        else:
            print("Invalid input. Please use Y/N")

    repeat = 1
    while (repeat == 1):
        hasLicense = input("Do you have a driver's license? (Y/N):  ")
        hasLicense = hasLicense.lower()
        if (hasLicense == 'y' or hasLicense == 'yes'):
            repeat = 0
        elif(hasLicense == 'n' or hasLicense == 'no'):
            print("You need to have a license in order to drive.")
            return 1
        else:
            print("Invalid input. Please us Y/N")

    print("You can drive a car!")
    return 0

main()
