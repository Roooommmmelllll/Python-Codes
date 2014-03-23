import turtle
import random

def drawRectangle(Turt):
   Turt.penup()
   randX = random.randint(-100,100)
   randY = random.randint(-100,100)
   Turt.goto(randX, randY)
   Turt.pendown()
   length = int(input("Please enter the length for the rectangle you want to draw:\n"))
   width = int(input("Please enter the width for the rectangle you want to draw:\n"))
   color = input("Please enter the color of the rectangle you want to draw:\n")
   Turt.pencolor(color)
   Turt.fillcolor(color)
   counter = 4
   Turt.begin_fill()
   while counter > 0:
      if(counter%2 == 0):
         Turt.forward(length)
         Turt.right(90)
      else:
         Turt.forward(width)
         Turt.right(90)
      counter -= 1
   Turt.end_fill()

def drawSquare(Turt):
   Turt.penup()
   randX = random.randint(-100,100)
   randY = random.randint(-100,100)
   Turt.goto(randX, randY)
   Turt.pendown()
   side = int(input("Please enter the length of a side for the square you want to draw:\n"))
   color = input("Please enter the color of the square you want to draw:\n")
   Turt.pencolor(color)
   Turt.fillcolor(color)
   counter = 4
   Turt.begin_fill()
   while counter > 0:
      Turt.forward(side)
      Turt.right(90)
      counter -= 1
   Turt.end_fill()

def drawCircle(Turt):
   Turt.penup()
   randX = random.randint(-100,100)
   randY = random.randint(-100,100)
   Turt.goto(randX, randY)
   Turt.pendown()
   Turt.begin_fill()
   radius = int(input("Please enter the radius for the circle you wish to draw:\n"))
   color = input("Please enter the color of the circle you wish to draw:\n")
   Turt.pencolor(color)
   Turt.fillcolor(color)
   Turt.circle(radius)
   Turt.end_fill()

def main():
   Turt = turtle.Turtle()
   user = input("Please enter the type of shape you want to draw (circle, square, or rectangle):\n")
   if (user == "square"):
      drawSquare(Turt)
   elif (user == "circle"):
      drawCircle(Turt)
   elif (user == "rectangle"):
      drawRectangle(Turt)

main()
