sometext = "asdkjaskjdnondgfjhjvjbyuytubkj gjjhbjghhbukyjbkuhjkuhbkujhjbkuygbkuybkuyhbkhjbghvfjjhjnkygjhkjhjnkkjkjhj"

foundA = False
foundB = False
count = 0

for x in sometext:
   print(x)
   if (foundA == False and x == "j"):
      print("Found first")
      foundA = True
   else:
      if (foundA == True and foundB == False and x == "h"):
         print("Found second")
         foundB = True
      elif (foundA == True and foundB == False and x != "h"):
         foundA = False
         print("Failed B")
      else:
         if (foundA == True and foundB == True and x == "j"):
            print("Found it!")
            count += 1
         else:
            foundA = False
            foundB = False
            print("Failed")


print("The substring 'jhj' was found", count, "times in the long string.")
      
   
