#the goal is to make a sailing game with turtle
import turtle
import os
import time
from math import *

#make the 2d field
wn=turtle.Screen()
wn.bgcolor("slate blue")
wn.title("Sail_Me_Silly")

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

#make whirl pool
wpensize = 5
whirl_pen=turtle.Turtle()
whirl_pen.speed(0)
whirl_pen.color("cornflower blue")
whirl_pen.penup()
whirl_pen.setposition(0,0)
whirl_pen.pendown()
segment_OG_len = .15
spiral_segment_length = segment_OG_len
for segment in range(200):
    whirl_pen.pensize(wpensize)
    whirl_pen.fd(spiral_segment_length)
    whirl_pen.lt(15)
    spiral_segment_length += segment_OG_len
    wpensize -= 1/200 * wpensize

whirl_pen.hideturtle()

#make the boat
pinta=turtle.Turtle()
pinta.penup()
pinta.color("grey1")
pinta.speed(0)
pinta.setposition(0,-250)
pinta.setheading(90)

class boat:
    def __init__(self):
        self.location=[0,-250]
        self.orientation=90
        self.rudder=0
        self.prop=0
        self.speed=0

    def accelerate(self):
        if self.prop<10:
            self.prop+=1
    def decelerate(self):
        if self.prop>-5:
            self.prop-=1
    def rudderR(self):
        if self.rudder<90:
            self.rudder+=1              # Should this be 10 instead of 1?
    def rudderL(self):
        if self.rudder>-90:
            self.rudder-=10             # or should this be 1 instead of 10?
prop=0
def accel():
    global prop
    if prop<4:
        prop+=.5

def decel():
    global prop
    if prop>-2:
        prop-=.5

def rudR():
    pinta.setheading(pinta.heading()-25)

def rudL():
    pinta.setheading(pinta.heading()+25)

def whirlpull():
    whirl_x = 0
    whirl_y = 0
    whirl_dist = sqrt((whirl_x - pinta.xcor())**2 + (whirl_y - pinta.ycor())**2)
    c = whirl_dist
    print(c)
    max_pull = 9
    pull_curve_intensity = 75 # Higher is more linear. Should be around 10 - 100.
    move_to_whirl = max_pull * 2.7**-(1/pull_curve_intensity * c)
    if pinta.xcor() != 0:
        whirl_slope = (pinta.ycor() - whirl_y)/(pinta.xcor() - whirl_x)
        adjust_x = move_to_whirl/sqrt(whirl_slope**2 + 1)
        adjust_y = whirl_slope * adjust_x
# Left side move to whirl
    if pinta.xcor() - whirl_x < 0 and whirl_dist > move_to_whirl:
        pinta.setx(pinta.xcor() + adjust_x)
        pinta.sety(pinta.ycor() + adjust_y)
# Right side move to whirl
    elif pinta.xcor() - whirl_x > 0 and whirl_dist > move_to_whirl:
        pinta.setx(pinta.xcor() + -adjust_x)
        pinta.sety(pinta.ycor() + -adjust_y)
# x = 0 move to whirl
    elif pinta.ycor() < 0 and whirl_dist > move_to_whirl:
        pinta.sety(pinta.ycor() + move_to_whirl)
    elif pinta.ycor() > 0 and whirl_dist > move_to_whirl:
        pinta.sety(pinta.ycor() - move_to_whirl)
# whirl_dist < move_to_whirl
    else:
        pinta.setx(whirl_x)
        pinta.sety(whirl_y)



windx=0
windy=0

while True:

    turtle.listen()
    turtle.onkey(accel, 'w')
    turtle.onkey(decel, 's')
    turtle.onkey(rudR, 'd')
    turtle.onkey(rudL, 'a')

    pinta.fd(prop)
    pinta.sety(pinta.ycor()+windy)
    pinta.setx(pinta.xcor()+windx)

    #boundries
    if pinta.xcor()>300:
        pinta.setx(300)
    if pinta.ycor()>300:
        pinta.sety(300)
    if pinta.xcor()<-300:
        pinta.setx(-300)
    if pinta.ycor()<-300:
        pinta.sety(-300)

    whirlpull()

#    time.sleep(.04)            # commented this out

#make rudder

#make wind

#make sail


delay=input("enter to quit")

