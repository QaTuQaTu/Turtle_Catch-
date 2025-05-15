from turtle import *
from random import randint
from time import sleep

# Connect the modules you need

# Create a "turtle" object, set the shape, color, and speed
t1 = Turtle()
t1.shape('turtle')
t1.color('red')
t1.speed(100)
t1.penup()

# Define a rand_move() function to move the turtle to a random point
def rand_move():
    t1.penup()
    t1.goto(randint(-90,50), randint(-20,45))

# Define a catch(x, y) handler function that will handle a click on the turtle
def catch(x, y):
    t1.write('A!', font=('Arial', 14, 'normal'))
    rand_move()

# Create a subscription to the «click on the turtle» event
t1.onclick(catch)

# Create a loop that runs as long as the t.points clicks are fewer than 3
while True:
    sleep(1.5)
    rand_move()

# Add the mainloop() function to start the event loop

mainloop()
