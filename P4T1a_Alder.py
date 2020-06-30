#Turtle Graphic P4T1a
#6/30/2020
#CTI-110 P4T1a - Shapes
#Branden Alder
#

import turtle

squares = 100                   #100 Squares
turtle.penup()                  #pen up to move location
turtle.goto(450,-400)           #move to bottom right
turtle.pendown()                #pen down to start drawing
side = sidesize = 30           #declare size of side for increase

for i in range(1, squares + 1): #For loop for drawing squares 
    turtle.left(90)             # Draw a Square
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    side = sidesize + 5 * i    # Increase the size of the side of the square

    turtle.goto(450,-400)       #go back




