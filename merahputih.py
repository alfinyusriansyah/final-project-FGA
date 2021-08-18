import turtle
from turtle import *
import sys
import time


#screen for output
screen = turtle.Screen()
speed(2)
 
# Defining a turtle Instance
t = turtle.Turtle()
 
# initially penup()
setup(700,500)
color("black")
bgcolor('black')


color('red')
begin_fill()
forward(300)
right(-90)
forward(200)
left(90)
forward(600)
left(90)
forward(200)
left(90)
forward(300)
end_fill()

color('white')
begin_fill()
forward(300)
right(90)
forward(200)
right(90)
forward(600)
right(90)
forward(200)
right(90)
forward(300)
position()
color('white')
time.sleep(1)
write("DIRGAHAYU REPUBLIK \n INDONESIA\n", font=("Calisto MT", 30, 'bold'), align='center')
end_fill()



setposition(0, -150)
color('red')
time.sleep(1)
write("Ke - 76", font=("Calisto MT", 80, 'bold'), align='center')


turtle.done()
