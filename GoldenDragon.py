from turtle import *
import math

space = Screen()
space.setup(width=1441, height=812, startx=None, starty=None)
space.colormode(255)
space.bgcolor(0,0,0)

bezos = Turtle()
bezos.hideturtle()
bezos.setundobuffer(0)
bezos.speed(0)

r = (2 / (1 + math.sqrt(5))) ** (2 / (1 + math.sqrt(5)))
A = math.acos(((2 / (1 + math.sqrt(5))) ** (4 / (1 + math.sqrt(5))) + 1 - (2 / (1 + math.sqrt(5))) ** (8 / (1 + math.sqrt(5)))) / (2 * (2 / (1 + math.sqrt(5))) ** (2 / (1 + math.sqrt(5)))))
C = math.acos(((2 / (1 + math.sqrt(5))) ** (8 / (1 + math.sqrt(5))) + (2 / (1 + math.sqrt(5))) ** (4 / (1 + math.sqrt(5))) - 1) / (2 * (2 / (1 + math.sqrt(5))) ** (4 / (1 + math.sqrt(5))) * (2 / (1 + math.sqrt(5))) ** (2 / (1 + math.sqrt(5)))))

lengths = [0]
directions = []
for i in range(15):
    subStep = []
    for i in directions:
        subStep.append(-i)
    directions.append(1)
    directions += subStep[::-1]
    newLengths = []
    for i in range(len(lengths)):
        if i % 2 == 0:
            newLengths.append(lengths[i] + 1)
            newLengths.append(lengths[i] + 2)
        else:
            newLengths.append(lengths[i] + 2)
            newLengths.append(lengths[i] + 1)
    lengths = newLengths

bezos.penup()
bezos.goto(-421.4396,-186.5356)
bezos.pendown()
bezos.radians()
bezos.left(A * lengths[0])
scale = 1000
bezos._tracer(0)
gradient = len(lengths)
thirdGradient = gradient / 3
quarterGradient = gradient / 4
for i in range(len(lengths)-1):
    red = 0
    green = 0
    blue = 0
    if i <= thirdGradient:
        red = (thirdGradient - i) / thirdGradient
    elif i >= 2 * thirdGradient:
        red = (i - 2 * thirdGradient) / quarterGradient
    if i <= thirdGradient:
        green = i / thirdGradient
    elif i <= 2 * thirdGradient:
        green = (2 * thirdGradient - i) / thirdGradient
    if i >= thirdGradient and i <= 2 * thirdGradient:
        blue = (i - thirdGradient) / thirdGradient
    elif i >= 2 * thirdGradient:
        blue = (gradient - i) / thirdGradient
    multiplier = 255/max(red,green,blue)
    red = round(red * multiplier)
    green = round(green * multiplier)
    blue = round(blue * multiplier)
    bezos.pencolor(red,green,blue)
    bezos.forward(r**lengths[i] * scale)
    if directions[i] == 1:
        bezos.right(math.pi - C)
    else:
        bezos.left(math.pi - C)
bezos.pencolor((255,0,0))
bezos.forward(r**lengths[-1] * scale)
bezos.penup()
bezos.goto(bezos.position())
bezos._update()
space.exitonclick()
