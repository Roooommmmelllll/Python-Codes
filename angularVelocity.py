def output(angularV, s):
   print("%8.2f"%s,"%18.2f"%angularV)

def angularVelocity(s):
   angularV = float(2*3.14*s/60)
   output(angularV, s)
   
def speed():
   s = float(1000)
   while (s <= 10000):
      angularVelocity(s)
      s += 1000

def main():
   print("  Speed\t\tAngular Velocity")
   speed()

main()
