V = 0
P = 0
T = 0

def calcMassFunction():
   M = ((P*V)/(0.42*(T+460)))
   return M

def outputFunction(M):
   print("A balloon with the\nVolume:", V)
   print("Pressure:", P, "\nTemperature: ", T)
   print("Has a mass of: ", M)
   
def main():
   global V
   global P
   global T
   print("This program computes the mass of a balloon.")
   V = int(input("Please enter the volume of the balloon.\n"))
   P = int(input("Please enter the pressure of the balloon.\n"))
   T = int(input("Please enter the temperature of the balloon.\n"))
   M = calcMassFunction()
   outputFunction(M)

main()
