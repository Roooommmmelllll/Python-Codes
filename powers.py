def exponent(base, power):
   if power == 0:
      return 1
   elif power > 0:
      return base*exponent(base,power-1)

def main():
   base = int(input("Enter a base value: "))
   power = int(input("Enter a power value: "))

   #answer = base**power
   #print(answer)

   recursionAnswer = exponent(base, power)
   print(answer2)
   
main()
