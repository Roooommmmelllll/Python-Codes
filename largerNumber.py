
def largeNumbers():
   value = 0
   for i in range(7):
      user = int(input("Please input seven numbers: "))
      if user > value:
         value = user
   print("The largest number you entered was: " + str(value) + ".")

largeNumbers()
