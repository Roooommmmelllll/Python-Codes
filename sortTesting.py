import random
import time

def randomGentenk():
   x = []
   for i in range (10000):
      rand = random.randint(0,10000)
      x.append(rand)
   return x

def randomGenfivek():
   x = []
   for i in range (5000):
      rand = random.randint(0,10000)
      x.append(rand)
   return x

def randomGentwofivek():
   x = []
   for i in range (2500):
      rand = random.randint(0,10000)
      x.append(rand)
   return x

def bubbleSort(lst):
   lst = list(lst)
##   timer = time.clock()
##   timeStamp = 1
   for passesLeft in range(len(lst)-1, 0, -1):
      for i in range(passesLeft):
         if lst[i] < lst[i + 1]:  
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
##         timer2 = time.clock()
##         checkTime = timer2-timer
##         if checkTime >= 1:
##            print(timeStamp)
##            timeStamp += 1
##            timer = time.clock()
   return lst  

def main():
   lst = randomGentenk()
   start = time.clock()
   bubbleSort(lst)
   fin = time.clock()
   timer = fin-start
   print(lst)
   print("Time:{:.6f}".format(timer), "seconds")
   
main()
