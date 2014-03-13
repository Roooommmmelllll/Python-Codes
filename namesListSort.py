def makeList():
   print("Input 5 names: ")
   for i in range(5):
      names.append(input())

def nameSort(names):
   names.sort()
   print(names)

def nameSortRev(names):
   names.reverse()
   print(names)

def main():
   names = []
   makeList(names)
   nameSort(names)
   nameSortRev(names)

main()
