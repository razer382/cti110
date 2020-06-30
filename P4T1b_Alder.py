#Turtle Initials
#6/30/2020
#CTI-110 P4T1b:Initials
#Branden Alder
#

import turtle

turtle.color('green') #Set color to green
turtle.pensize(5)     #Change pen size
turtle.speed(5)

turtle.left(90) 
turtle.forward(200)   #Draw the straight line in B
turtle.right(90)
turtle.forward(20)
for x in range(160):  #Using for loop to draw the circular part in the B
    turtle.forward(1)
    turtle.right(1)
turtle.left(150)      #change angle to make the other circular part of the B
for x in range(160):  #Draw the 2nd circular part of the B
    turtle.forward(1)
    turtle.right(1)
turtle.right(10)
turtle.forward(42)
turtle.right(90)
turtle.forward(25)

turtle.penup()          #pen up to move location
turtle.goto(180,-10)
turtle.pendown()

turtle.right(20)
turtle.forward(200)
turtle.right(135)
turtle.forward(200)
turtle.backward(100)
turtle.right(115)
turtle.forward(80)
