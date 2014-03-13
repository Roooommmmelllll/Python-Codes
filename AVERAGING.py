def average():
   input1 = 1
   total = 0
   totalInputs = 0
   average = 0
   while input1 != 0:
      input1 = float(input("Input a value for BEWD"))
      totalInputs +=1
      average += input1
   average /= totalInputs

   print("The average for those card inputs is: " + str(average))
