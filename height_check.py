def heightCheck():
    print("This program will check your height!")
    again = True
    while again == True:
        repeat = True
        while repeat == True:
            feet = input("How tall are you in feet?")
            if feet.isdigit() == True:
                feet = int(feet)
                if feet < 2 or feet > 9:
                    print("Invalid input, you are not that short or tall")
                else:
                    break
            else:
                print("Your input is not a number. Try again.")
        while repeat == True:
            inches = input("How tall are you in inches?")
            if inches.isdigit() == True:
                inches = int(inches)
                if inches < 0 or inches > 12:
                    print("Invalid input, use correct inches.")
                else:
                    break
            else:
                print("Your input is not a number. Try again.")
        height=(feet*12)+inches
        print("You are " + str(height) + " inches tall.")
        if height < 60:
            print("You are unfortunately short.")
        elif height >= 60 and height <= 72:
            print("You are averagely average.")
        else:
            print("You are luckily tall.")
        while repeat == True:
            ask = input("Do you want to repeat this program again? (yes or no)")
            ask = ask.lower()
            if ask == "yes" or ask == "y":
                again = True
                break
            elif ask == "no" or ask == "n":
                again = False
                print("Thank you. Come Again.")
                break
            else:
                print("That is an invalid input. Please use Yes or No")
                
heightCheck()        
