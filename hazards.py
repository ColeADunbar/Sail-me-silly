# this is the function definitions for the hazards that can be placed
import turtle
from math import *

def weathervane(angle,power):
    vane=turtle.Turtle()
    vane.speed(0)
    vane.penup()
    vane.setposition(295,295)
    vane.setheading(angle)
    vane.pendown()
    vane.write(power)
    vane.shape("turtle")
    return

def windpull(boat, angle, power):
    angle=radians(angle)
    boat.sety(boat.ycor()+sin(angle)*power)
    boat.setx(boat.xcor()+cos(angle)*power)
    return

def whirlpool(x,y):
    #make whirl pool
    wpensize = 5
    whirl_pen=turtle.Turtle()
    whirl_pen.hideturtle()
    whirl_pen.speed(0)
    whirl_pen.color("cornflower blue")
    whirl_pen.penup()
    whirl_pen.setposition(x,y)
    whirl_pen.pendown()
    segment_OG_len = .15
    spiral_segment_length = segment_OG_len
    for segment in range(200):
        whirl_pen.pensize(wpensize)
        whirl_pen.fd(spiral_segment_length)
        whirl_pen.lt(15)
        spiral_segment_length += segment_OG_len
        wpensize -= 1/200 * wpensize


def whirlpull(pinta):
    whirl_x = 0
    whirl_y = 0
    whirl_dist = sqrt((whirl_x - pinta.xcor())**2 + (whirl_y - pinta.ycor())**2)
    c = whirl_dist
    #print(c)
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


