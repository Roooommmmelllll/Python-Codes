def main():
   user = input("Please enter a sentence.\n")
   letter = input("Please enter a letter to count in that sentence.\n")
   count = 0
   for i in range(len(user)):
      if(user[i] == letter):
         count+= 1
   print("In the sentence:\n", user, "\nThe letter", letter,
         "appears", count, "times.")

main()
