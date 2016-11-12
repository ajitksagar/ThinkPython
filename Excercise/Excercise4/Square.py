import math

from swampy.TurtleWorld import *

def square(t,length):
    for i in range(4):
        fd(t,length)
        lt(t)

def polygon(t,length,n):
    for i in range(n):
        fd(t,length)
        lt(t,360/n)

def polyline(t,length,n,angle):
    for i in range(n):
        fd(t,length)
        lt(t,angle)

def circle(t,r):
    circumferance = 2 * 3.14 * r
    n=50
    length = circumferance / 50
    polygon(t,length,n)

def arc(t,r,angle):
    arc_length= 2 * math.pi * r * angle / 360
    n = int(arc_length/3) + 1
    step_length = arc_length/n
    step_angle = float(angle)/n

    polyline(t,step_length,n,step_angle)

    lt(t,90)
    fd(t,r)
    lt(t,180-angle)
    fd(t,r)

world = TurtleWorld()
bob = Turtle()

# square(bob,50)

# polygon(bob,50,8)

#circle(bob,30)

arc(bob,60,45)