#Program will ask user to input 5 integers.
#The integers should be added to a list named "numbers".
#The program will then go through the list and divide
#each number by 2. the Output will show the original
#list as well as the list after the divisions.

def genList():
   numbers = []
   print("Please enter 5 integers")
   for i in range(5):
      testing = 1
      while testing == 1:
         try:
            numbers.append(int(input()))
            break
         except ValueError:
            print("That is not a valid integer.")
   return numbers

def divide(numbers):
   divNumber = []
   for i in range(5):
      divNumber.append(numbers[i]/2)
   return divNumber

def main():
   numbers = genList()
   divNumber = divide(numbers)
   print("The original list:", numbers)
   print("The divided list:", divNumber)
   
main()
