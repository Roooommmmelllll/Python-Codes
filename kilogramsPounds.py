# WRITE A PROGRAM THAT DISPLAYS A TABLE
# THAT CONVERTS KILOGRAMS TO POUNDS.
# FROM 1 KILOGRAM TO 199 KILOGRAMS.
# 1 KILOGRAM IS EQUAL TO 2.2 POUNDS.

def kilogramsPounds():
   print("KILOGRAMS\tPOUNDS")
   for kilos in range (1,200):
      pounds = kilos*2.2
      print(str(kilos)+"\t\t"+'%.2f'%(pounds))

kilogramsPounds()
