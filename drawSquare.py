import turtle

def drawCircle():
   radius = int(input("What is the radius of the circle you want?: "))
   bob = turtle.Turtle()
   bob.circle(radius)

def drawSquare():
   sides = 4
   angle = 90
   length = int(input("What is the length of the sides of the square you want?: "))
   bob = turtle.Turtle()
   while sides > 0:
      bob.forward(length)
      bob.left(angle)
      sides-= 1

def drawRectangle():
   sides = 4
   angle = 90
   length = int(input("What is the length of the sides of the square you want?: "))
   width = int(input("What is the width of the sides of the square you want?: "))
   bob = turtle.Turtle()
   while sides > 0:
      if sides%2 == 0:
         bob.forward(length)
         bob.left(angle)
         sides-=1
      else:
         bob.forward(width)
         bob.left(angle)
         sides-=1

def main():
   choice = input("What kind of shape do you wish to draw? (circle, square, or rectangle): ")
   if choice
