import turtle

def smiley():
   #generate turtle screen
   bob = turtle.Turtle()

   #draw main face circle
   bob.penup()
   bob.goto(0,0)
   bob.pendown()
   bob.circle(100)

   #draw nose line
   bob.penup()
   bob.goto(0,90)
   bob.pendown()
   bob.goto(0,60)

   #draw right eye Blue
   bob.penup()
   bob.goto(40,120)
   bob.pendown()
   bob.color("blue")
   bob.circle(10)

   #draw left eye Green
   bob.penup()
   bob.goto(-40,120)
   bob.pendown()
   bob.color("green")
   bob.circle(10)

   #draw mouth
   bob.penup()
   bob.goto(-60,50)
   bob.pendown()
   bob.color("black")
   bob.right(50)
   bob.circle(80,100)

smiley()
