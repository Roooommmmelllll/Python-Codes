def convKG(pounds):
   kilograms = pounds*0.453592
   print(pounds, "pounds =", kilograms, "kilograms")

def convLB(kilograms):
   pounds = kilograms*2.20462
   print(kilograms, "kilograms =", pounds, "pounds")

def convMI(kilometers):
   miles = kilometers*1.60934
   print(kilometers, "kilometers =", miles, "miles")

def convKM(miles):
   kilometers = miles*.621371
   print(miles, "miles =", kilometers, "kilometers")

def choosing():
   print("Please choose an option:")
   print("1) Convert kilograms to pounds")
   print("2) Convert pounds to kilograms")
   print("3) Convert miles to kilometers")
   print("4) Convert kilometers to miles")
   convertType = int(input())
   value = int(input("Please enter the value to convert: "))

   if(convertType == 1):
      convLB(value)
   elif(convertType == 2):
      convKG(value)
   elif(convertType == 3):
      convKM(value)
   elif(convertType == 4):
      convMI(value)

def main():
   again = "y"
   while (again == "y"):
      choosing()
      again = input("Repeat program? (y or n)")

main()
