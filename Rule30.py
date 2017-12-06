from turtle import *

scale = 1

space = Screen()
space.setup(width=600, height=600, startx=None, starty=None)
space.colormode(255)
space.bgcolor(0,255,255)

bezos = Turtle()
bezos.hideturtle()
bezos.setundobuffer(None)
bezos.pensize(scale)

def render(renderer, entities):
    renderer._tracer(1000000,0)
    for i in entities:
        renderer.penup()
        pos = (i[0] * scale,i[1] * scale)
        renderer.setposition(pos)
        renderer.pendown()
        renderer.setposition(pos)

testArea = ((-1,1),(0,1),(1,1))

initialState = [(0,100)]

previousLine = set(initialState)

startX = initialState[0][0]
yPos = initialState[0][1]

render(bezos,previousLine)

for frame in range(405):

    startX -= 1
    yPos -= 1

    currentLine = set()

    for i in range(startX, abs(startX) + 1):
        if (i + testArea[0][0],yPos + testArea[0][1]) in previousLine:
            if (i + testArea[1][0],yPos + testArea[1][1]) not in previousLine:
                if (i + testArea[2][0],yPos + testArea[2][1]) not in previousLine:
                    currentLine.add((i,yPos))
        elif (i + testArea[1][0],yPos + testArea[1][1]) in previousLine:
            currentLine.add((i,yPos))
        elif (i + testArea[2][0],yPos + testArea[2][1]) in previousLine:
            currentLine.add((i,yPos))

    render(bezos,currentLine)

    previousLine = currentLine

space.exitonclick()
