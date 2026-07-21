import turtle

t=turtle.Turtle()
t.begin_fill()
t.circle(100)

t.penup()
t.goto(-40,120)
t.pendown()
t.circle(20)

t.penup()
t.goto(40,120)
t.pendown()
t.circle(20)

t.penup()#Task1: Make Smiley using the knowledge from Activity 2.4
t.right(90)
t.forward(50)#Task2: Give the smiley face your favorite color
t.right(90)
t.forward(90)
t.left(90)
t.pendown()
t.circle(50,180)
t.penup()
t.forward(60)
t.left(90)
t.forward(100)
t.color("yellow")
t.end_fill()
# Write your code here :-)

# Write your code here :-)
