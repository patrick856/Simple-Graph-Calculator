import turtle
import math

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")" 
    
    def inRange(self):
        return abs(self.x) <= width/2 and abs(self.y) <= length/2


def f(x): # equation 
    x /= 10
    return (2 * x ** 3 - 5 * x ** 2 + 2 * x) * 10 
    return x ** 2 * 10
    return math.sin(x) * 10 
    return x + 1

def derivative(x): # d/dx of the equation
    x /= 10
    return 6 * x ** 2 - 10 * x + 2
    return 2 * x
    return math.cos(x)
    return 1

def distance(point1, point2):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

def setCoordinates(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

width, length = 600, 600

screen = turtle.Screen()
screen.screensize(width,length)
turtle.bgcolor('black')

t = turtle.Turtle()
t.speed(0)
t.color('white')
t.sety(length/2)
t.setheading(270)
t.forward(length)
t.sety(0)
t.setx(-length/2)
t.setheading(0)
t.forward(length)
t.color('purple')

scale = 1

xstart = -length/2
ystart = f(xstart)
point1 = point(xstart, ystart)

if point1.inRange():
    setCoordinates(point1.x, point1.y)
else:
    for x in range(int(xstart), int(length/2), scale):
        point1 = point(x, f(x))
        if point1.inRange():
            setCoordinates(point1.x, point1.y)
            break

for x in range(int(point1.x + scale), int(length/2 - scale), scale):
    point1 = point(x,f(x))
    point2 = point(x + scale, f(x + scale))
    if not point1.inRange(): continue
    angle = math.degrees(math.atan(derivative((point1.x+point2.x)/2)))
    t.setheading(angle) 
    t.forward(distance(point1, point2))

wait = input("DONE!") 