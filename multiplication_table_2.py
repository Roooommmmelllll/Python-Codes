def multiTable():
   for vert in range(1,13):
      line = ""
      for horiz in range(1,13):
         line += str("%5.0f"%(vert*horiz))
      print(line)

def main():
   multiTable()

main()
