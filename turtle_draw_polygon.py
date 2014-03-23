import turtle
   
def main():
   Turt = turtle.Turtle()
   sides = int(input("How many sides do you want the polygon to have:\n"))
   length = int(input("What is the length of the sides you want the polygon to have:\n"))
   color = input("Please enter the color of the rectangle you want to draw:\n")
   Turt.pencolor(color)
   Turt.fillcolor(color)
   Turt.begin_fill()
   angle = sides
   while sides > 0:
      Turt.forward(length)
      Turt.right(360/angle)
      sides -= 1
   Turt.end_fill()

main()
