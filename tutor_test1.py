#print a conversion table from kilograms to pounds
#print every odd number from 1 - 199 in kilograms
#and convert. Kilograms to the left and pounds to the right

def conversionTable():
   print("Kilograms         Pounds")
   #2.2 pound = 1kilograms
   kilograms = 1
   kilograms = float(kilograms)
   while kilograms <= 199:
      pounds = kilograms*2.2
      print(str("%4.2f"%kilograms) + str("%20.2f"%pounds))
      kilograms += 2

conversionTable()
