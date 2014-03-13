#Use a "while" loop to find the largest
#integer n such that n^3 is less than 12000

def cubed():
   n = 1
   n3 = 1
   #n^3 < 12000

##   while n3 <= 12000:
##      n3 = n**3
##      if n3 >= 12000:
##         n-=1
##         break
##      else:
##         n+=1

   for i in range(1,12000):
      n3 = i**3
      if n3 >= 12000:
         n = i-1
         break

   print(n, "is the largest value for n such that n^3 is less than 12000, where",
         n**3, "is the value.")

cubed()
