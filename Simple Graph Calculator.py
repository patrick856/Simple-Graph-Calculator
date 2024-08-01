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
    x /= upscaleRatio
    equation = 3 + (100 - (x - 3) ** 2) ** 0.5 * signIndex
    if isinstance(equation, complex): return 1000000
    return  round(equation * upscaleRatio, 2)

def derivative(x): # d/dx of the equation
    x /= upscaleRatio
    dydx = (-x + 3)/((100 - (x - 3) ** 2) ** 0.5)
    return dydx * signIndex

def distance(point1, point2):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

def setCoordinates(x, y):
    pen1.penup()
    pen1.goto(x, y)
    pen1.pendown()

# changable variables to match the equations and user needs
width, length = 600, 600                    # graph size
step = 1                                    # step between each point
upscaleRatio = 15                           # upscales/downscales the graph while the window size is constant
equationIsPostiveOrNegative = True          # pretty self expresive?
signIndex = 1                               # this should be one and the code changes it when needed

screen = turtle.Screen()
screen.screensize(width,length)
turtle.bgcolor('black')

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color('white')
pen1.sety(length/2)
pen1.setheading(270)
pen1.forward(length)
pen1.sety(0)
pen1.setx(-length/2)
pen1.setheading(0)
pen1.forward(length)
pen1.color('purple')

while True:
    xstart = -length/2
    ystart = f(xstart)
    point1 = point(xstart, ystart)

    if point1.inRange():
        setCoordinates(point1.x, point1.y)
    else:
        for x in range(int(xstart), int(length/2), step):
            point1 = point(x, f(x))
            if point1.inRange():
                setCoordinates(point1.x, point1.y)
                break

    for x in range(int(point1.x), int(length/2 - step), step):
        point1 = point(x,f(x))
        point2 = point(x + step, f(x + step))
        if not point1.inRange() or not point2.inRange(): continue
        angle = math.degrees(math.atan(derivative((point1.x+point2.x)/2)))
        pen1.setheading(angle) 
        pen1.forward(distance(point1, point2))
    if equationIsPostiveOrNegative:
        signIndex = -1
        equationIsPostiveOrNegative = False
    else: break

wait = input("DONE!") 