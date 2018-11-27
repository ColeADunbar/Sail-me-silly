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
bound_pen.speed(10)
bound_pen.color("white")
bound_pen.penup()
bound_pen.setposition(-300,-300)
bound_pen.pendown()
bound_pen.pensize(3)
for side in range(4):
    bound_pen.fd(600)
    bound_pen.lt(90)
bound_pen.hideturtle()

#create boundry matrix
boundMat=[[[0 for xy in range(2)] for col in range(6)] for row in range(6)]

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
whirl_location=[]
pull=0
def whirl():
    global whirl_location
    global pull
    whirl_location.append([random.randint(-200,200),random.randint(-200,200)])
    hazards.whirlpool(whirl_location[pull][0],whirl_location[pull][1])
    pull+=1

windAngle=180
windForce=1
hazards.weathervane(windAngle,windForce)


def island_build():
    hazards.island(random.randint(-300,300),random.randint(-300,300))

while True:

    turtle.listen()
    turtle.onkey(accel, 'Up')
    turtle.onkey(decel, 'Down')
    turtle.onkey(lambda: pinta.right(25), 'Right')
    turtle.onkey(lambda: pinta.left(25), 'Left')
    turtle.onkey(island_build,'i')
    turtle.onkey(whirl, 'v')

    #boat movement
    pinta.fd(prop)
    pinta.write(prop)
    hazards.windpull(pinta, windAngle,windForce)

    #hit v to place a whirlpool
    for i in whirl_location:
        hazards.whirlpull(pinta, i[0], i[1])

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

