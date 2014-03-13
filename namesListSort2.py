# Write a program that has the user input
# 5 names, first and last. After all the
# input are done, the program will put the
# list into alphabetical order by first name.
# The program will then put the list in
# reverse alphabetical order. The program
# will then put the list in order by last name.

def makeList():
   print("Input 5 names, first and last name: ")
   for i in range(5):
      names.append(input())

def nameSort(names):
   names.sort()
   for i in range(len(names)):
      print(names[i])

def nameSortRev(names):
   names.reverse()
   for i in range(len(names)):
      print(names[i])

def lastSort(names):
   lasts = []
   for i in range(len(names)):
      currentName = names[i]
      space = currentName.find(" ")
      lasts.append(currentName[space+1])

def main():
   names = []
   makeList()
   nameSort(names)
   nameSortRev(names)
   lastSort(names)

main()
