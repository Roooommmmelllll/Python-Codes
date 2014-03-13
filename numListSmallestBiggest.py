# Write a program that will randomly generate
# 20 integers between 0 and 100. The program
# will pick out the smallest of the numbers
# and the largest of the numbers. The output
# will show the randomly generated list, and
# the smallest and largest values found in
# that list. You do not get credit for this
# one if you use the python sort() function.

import random

def smallestBiggest():

   numbers = []
   for i in range(20):
      numbers.append(random.randint(0,100))

   largest = numbers[0]
   smallest = numbers[0]

   for i in range(20):
      if numbers[i] > largest:
         largest = numbers[i]
      if numbers[i] < smallest:
         smallest = numbers[i]
   
   print("In the list:\n", numbers) 
   print("The smallest number is", smallest)
   print("The largest number is", largest)
   
smallestBiggest()
