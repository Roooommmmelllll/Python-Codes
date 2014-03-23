W = 0
H = 0
D = 0

def setW(w):
   global W
   W = w

def setH(h):
   global H
   H = h
   
def setD(d):
   global D
   D = d

def calcVolume():
   volume = W*H*D
   return volume

def main():
   print("This program calculate the volume of a rectangular prism.")
   w = int(input("Enter the prism's width:\n"))
   h = int(input("Enter the prism's height:\n"))
   d = int(input("Enter the prism's depth:\n"))
   setW(w)
   setH(h)
   setD(d)
   print("The prism with dimensions:",W, "x", H, "x", D,
         " has a volume of", str(calcVolume())+".")

main()
