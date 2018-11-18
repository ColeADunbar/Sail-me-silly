#the goal is to make a sailing game with turtle
import turtle
import os
import time

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
            self.rudder+=1
    def rudderL(self):
        if self.rudder>-90:
            self.rudder-=10
prop=0
def accel():
    global prop
    if prop<10:
        prop+=1

def decel():
    global prop
    if prop>-5:
        prop-=1

def rudR():
    pinta.setheading(pinta.heading()-5)

def rudL():
    pinta.setheading(pinta.heading()+5)

windx=0
windy=-3

while True:

    turtle.listen()
    turtle.onkey(accel, 'w')
    turtle.onkey(decel, 's')
    turtle.onkey(rudR, 'd')
    turtle.onkey(rudL, 'a')

    pinta.fd(prop)
    pinta.sety(pinta.ycor()+windy)

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

#make wind

#make sail


delay=input("enter to quit")
