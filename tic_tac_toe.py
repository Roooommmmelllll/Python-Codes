import turtle

def printBoard(gameBoard0, gameBoard1, gameBoard2, gameBoard3):
    i = 0
    while (i < 1):
        print (gameBoard0[i])
        i = i + 1
    i = 0
    while (i < 1):
        print (gameBoard1[i])
        i = i + 1
    i = 0
    while (i < 1):
        print (gameBoard2[i])
        i = i + 1
    i = 0
    while (i < 1):
        print (gameBoard3[i])
        i = i + 1

def p1CommandLine(gameBoard1, gameBoard2, gameBoard3):
    endIt = 0
    while endIt == 0:
        p1Row = int(input("\nPlayer ONE please input a number for the row (top to bottom 1 - 3)"))
        if p1Row < 1:
            print("You cannot place a guess there! It doesn't exist!")
        elif p1Row > 3:
            print("You cannot place a guess there! It doesn't exist!")
        else:
            p1Column = int(input("Player ONE please input a number for the column (left to right 1 - 3)"))
            if p1Column < 1:
                print("You cannot place a guess there! It doesn't exist!")
            elif p1Column > 3:
                print("You cannot place a guess there! It doesn't exist!")
            elif p1Row == 1:
                gameBoard1[p1Column] = 'X'
                endIt = 1
            elif p1Row == 2:
                gameBoard2[p1Column] = 'X'
                endIt = 1
            elif p1Row == 3:
                gameBoard3[p1Column] = 'X'
                endIt = 1
                
def p2CommandLine(gameBoard1, gameBoard2, gameBoard3):
    p2Row = int(input("Player TWO please input a number for the row (top to bottom)"))
    p2Column = int(input("Player TWO please input a number for the column (left to right"))

def exitCommandLine():
    print("\n1. Clear the board and start a new game.")
    print("2. Exit the Game.")
    cmd = input("Please input a number for the command: ")

def mainCommandLine(gameBoard1, gameBoard2, gameBoard3):
    winner = 0
    p1CommandLine(gameBoard1, gameBoard2, gameBoard3)
    p2CommandLine(gameBoard1, gameBoard2, gameBoard3)

def main():
    print("You are playing a game of Tic Tac Toe with a friend.")
    print("Choose who goes first; however you wish.\n")
    gameBoard0 = [('  '' 1 '' 2 '' 3 ')]
    gameBoard1 = [('1 '' _ '' _ '' _ ')]
    gameBoard2 = [('2 '' _ '' _ '' _ ')]
    gameBoard3 = [('3 '' _ '' _ '' _ ')]
    printBoard(gameBoard0, gameBoard1, gameBoard2, gameBoard3)
    mainCommandLine(gameBoard1, gameBoard2, gameBoard3)

main()
