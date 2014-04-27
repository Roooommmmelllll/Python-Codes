def checkPal(norm):
   palindrome = norm[::-1]
   if(norm == palindrome):
      print("\nIt's a palindrome!\n")
   else:
      print("\nThat is not a palindrome!\n")

def main():
   again = 1
   while (again == 1):
      norm = input("\nPlease enter a word:  ")
      checkPal(norm)
      again = int(input("Use again? (1 for yes, 0 for no):  "))

main()
