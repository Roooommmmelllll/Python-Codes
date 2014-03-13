import turtle

def drawPolygon():
   
   sides = int(input("How many sides do you want to give the polygon?"))
   bob = turtle.Turtle()
   angle = 360/sides

   addAngle = angle
   length = 40
   counter = 0
   
   bob.penup()
   bob.goto(-120,-120)
   bob.pencolor("purple")
   bob.pendown()
   while counter < sides:
      bob.forward(length)
      bob.setheading(angle)
      angle+= addAngle
      counter += 1
      
drawPolygon()
