def rentbus():

   people = int(input("How many people are going?: "))
   extra = people - 34
   if extra >= 0:
      print(extra, "people need to drive.")
   else:
      extra *= -1
      print("There are", extra, "spaces empty on the bus.")
   
