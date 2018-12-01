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
boundMat=[[[0 for xy in range(2)] for col in range(650)] for row in range(650)]

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


island_location=[]
island_count=0
def island_build():
    global island_location
    global island_count
    island_location.append([random.randint(-300,300),random.randint(-300,300),random.randint(10,40)])
    x=island_location[island_count][0]
    y=island_location[island_count][1]
    radius=island_location[island_count][2]
    hazards.island(x, y-radius, radius)
    island_count+=1
    #update boundmat TODO this is a project for later


windAngle=0
windForce=0
def wind():
    global windAngle
    global windForce
    windAngle=random.randint(0,359)
    windForce=random.randint(0,5)
    hazards.weathervane(windAngle,windForce)

def goal():
    goal1=hazards.zone(0,0,20)
    goal1.draw("green")

while True:

    turtle.listen()
    turtle.onkey(accel, 'Up')
    turtle.onkey(decel, 'Down')
    turtle.onkey(lambda: pinta.right(25), 'Right')
    turtle.onkey(lambda: pinta.left(25), 'Left')

    #boat movement
    for i in range(prop):
        pinta.fd(1)
    pinta.write(".")

    #hit i to place an island WARNING this must be right after write and fd
    turtle.onkey(island_build,'i')
    for i in island_location:
        hazards.islandpull(pinta, i[0],i[1],i[2])

    #hit g to place a goal
    turtle.onkey(goal, 'g')
    try:
        if goal1.active:
            goal1.force(pinta)
            print("goal!")
    except NameError:
        pass

    #hit w to change the wind
    turtle.onkey(wind, 'w')
    for i in range(windForce):
        hazards.windpull(pinta, windAngle,1)


    #hit v to place a whirlpool
    turtle.onkey(whirl, 'v')
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

    pinta.write(prop)
    time.sleep(.04)
    pinta.undo()
#make rudder

#make sail

