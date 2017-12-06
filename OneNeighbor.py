from turtle import *

scale = 1

space = Screen()
space.setup(width=600, height=600, startx=None, starty=None)
space.colormode(255)
space.bgcolor(255,255,255)

bezos = Turtle()
bezos.hideturtle()

def render(renderer, entities):
    renderer._tracer(1000000,0)
    renderer.setundobuffer(None)
    renderer.pensize(scale)
    for i in entities:
        renderer.penup()
        pos = (i[0] * scale,i[1] * scale)
        renderer.setposition(pos)
        renderer.pendown()
        renderer.setposition(pos)

testArea = ((-1,-1),(-1,0),(0,-1),(-1,1),(1,-1),(0,1),(1,0),(1,1))

newCells = [(0,0)]

positions = set(newCells)

shouldBreak = False

render(bezos,newCells)

for frame in range(127):

    affectedCells = set()
    for cell in newCells:
        for displacement in testArea:
            affectedCells.add((cell[0] + displacement[0],cell[1] + displacement[1]))

    newCells = []

    for cell in affectedCells:
        neighbors = 0
        for displacement in testArea:
            if (cell[0] + displacement[0],cell[1] + displacement[1]) in positions:
                neighbors += 1
                if neighbors > 1:
                    break
        if neighbors == 1:
            newCells.append(cell)

    for newCell in newCells:
        positions.add(newCell)

    render(bezos,newCells)

space.exitonclick()
