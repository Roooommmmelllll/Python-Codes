import itertools
import hashlib

def main():
   #Original Data
   name = "Jane Doe Smith"
   bd = "02/13/1981"
   ssn = "567-33-2013"
   pn = "831.228.5671"
   petName = "Kujo Friendly"
   win7Pass = "ae2e1fa899105c28184c0d0d11be8241"

   print("The Original Data")
   print(name,"\n",bd,"\n",ssn,"\n",pn,"\n",petName,"\n")
   
   #Splits Data into Lists
   nameStr = name.split(" ")
   bdStr = bd.split("/")
   ssnStr = ssn.split("-")
   pnStr = pn.split(".")
   petNameStr = petName.split(" ")

   print("The String Form Data")
   print(nameStr,"\n",bdStr,"\n",ssnStr,"\n",pnStr,"\n",petNameStr,"\n")

   #Combines all the lists into one big list
   bigList = nameStr + bdStr + ssnStr + pnStr + petNameStr

   print("The Combined Data List")
   print(bigList)

   #Permutates the pieces of the list into single strings and puts them in a list
   perms = itertools.permutations(bigList, r=3)
   permsList = list(perms)

   print("The list pieces have been separated into sets of 3.")

   #Finds the password!
   print("\n\nNow looking for password.")
   
   correctPass = "" #Holds password if found.
   correctHash = "" #Holds the password hash if found.
   tries = 0
   
   for i in range(len(permsList)):
      
      #turns the generated password into MD5 hex
      joinedItem = ''.join((permsList[i]))
      joinItemByte = joinedItem.encode('utf-8')
      joinItemMD5 = hashlib.md5(joinItemByte)
      joinItemDigest = joinItemMD5.hexdigest()

      #keeps check of the tries
      tries += 1
      
      #checks against the taken password
      if win7Pass == joinItemDigest:
         correctPass = joinedItem
         correctHash = joinItemDigest
         print("Password found!")
         break

   print("\nThe Hashed MD5:", correctHash)
   print("\nThe password is:", correctPass)
   print("\nIt only took", tries, "tries!")

main()
