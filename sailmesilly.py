#the goal is to make a sailing game with turtle
import turtle
import os
import time
from math import *
import hazards as hazards
import random

#make the 2d field
wn=turtle.Screen()
wn.bgcolor("slate blue")
wn.title("Sail_Me_Silly")
wn.setup(650,650)

#make a border
bound_pen=turtle.Turtle()
bound_pen.speed(0)
bound_pen.color("white")
bound_pen.penup()
bound_pen.setposition(-300,-300)
bound_pen.pendown()
bound_pen.pensize(3)
for side in range(4):
    bound_pen.fd(600)
    bound_pen.lt(90)
bound_pen.hideturtle()


#make the boat
pinta=turtle.Turtle()
pinta.penup()
pinta.color("grey1")
pinta.speed(0)
pinta.setposition(0,-250)
pinta.setheading(90)

prop=0
def accel():
    global prop
    if prop<10:
        prop+=1

def decel():
    global prop
    if prop>-3:
        prop-=1


#draw the whirlpool at whirl_x, whirl_y if you press p
pull=False
whirl_x=0
whirl_y=0
def whirl():
    global whirl_x
    whirl_x=random.randint(-200,200)
    global whirl_y
    whirl_y=random.randint(-200,200)
    hazards.whirlpool(whirl_x,whirl_y)
    global pull
    pull=True


hazards.weathervane(45,2)


def island_build():
    hazards.island(random.randint(-300,300),random.randint(-300,300))

while True:

    turtle.listen()
    turtle.onkey(accel, 'w')
    turtle.onkey(decel, 's')
    turtle.onkey(lambda: pinta.right(25), 'd')
    turtle.onkey(lambda: pinta.left(25), 'a')
    turtle.onkey(island_build,'i')
    turtle.onkey(whirl, 'v')

    #boat movement
    pinta.fd(prop)
    pinta.write(prop)
    hazards.windpull(pinta, 45, 2)

    #hit v to place a whirlpool
    if pull:
        hazards.whirlpull(pinta)

    #boundries
    if pinta.xcor()>300:
        pinta.setx(300)
    if pinta.ycor()>300:
        pinta.sety(300)
    if pinta.xcor()<-300:
        pinta.setx(-300)
    if pinta.ycor()<-300:
        pinta.sety(-300)

    time.sleep(.04)

#make rudder

#make sail

