def testing1():
    judges = 4
    total = 0
    while judges > 0:
        score = int(input("Input Judge " + str(judges) + "'s score: "))
        if score <= 0 or score > 10:
            print("Invalid score. Please try again.")
        else:
            total += score
            judges -= 1
    average = total / 4
    print("The average score from all judges is " + str(average) + ".")

def checkNegPos():
    userInput = 1
    even = 0
    odd = 0
    while userInput != 0:
        userInput = int(input("Please input an integer"))
        if userInput == 0:
            break
        else:
            if (userInput % 2) == 0:
                even += 1
            else:
                odd += 1
        
checkNegPos()
