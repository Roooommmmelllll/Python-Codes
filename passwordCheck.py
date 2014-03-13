def getPass():
   print("Please enter a password that is at" +
         " least 8 characters long.")
   print("The password must have at least one" +
         " capital letter.")
   print("The password must have at least one" +
         " lower case letter.")
   print("The password must have at least one" +
         " special character" +
         " (not a letter or number).")
   password = input()
   return password

def checkPass(password):
   length = 1
   cap = 0
   low = 0
   special = 0
   
   if (len(password) < 8):
      length = 0
   for i in range(len(password)):
      if (password[i].isupper() == True and cap == 0):
         cap = 1
      if (password[i].islower() == True and low == 0):
         low = 1
      if (special == 0): 
         if (password[i] == "!" or password[i] == "@" or
             password[i] == "#" or password[i] == "$" or
             password[i] == "%" or password[i] == "^" or
             password[i] == "&" or password[i] == "*"):
            special = 1
   if (length == 0):
      print("The password is too short.")

   if (cap == 0):
      print("The password does not have a capital letter in it.")

   if (low == 0):
      print("The password does not have a lower case letter in it.")

   if (special == 0):
      print("The password does not have a special character in it.")

   if (length == 0 or cap == 0 or low == 0 or special == 0):
      return False
   else:
      return True

def main():
   loop = 1
   while (loop == 1):
      password = getPass()
      checked = checkPass(password)
      print("\n")
      if (checked == True):
         break
   print("Password accepted. Thank you.")

main()
