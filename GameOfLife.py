from turtle import *
import time

scale = 5

space = Screen()
space.setup(width=600, height=600, startx=None, starty=None)
space.colormode(255)
space.bgcolor(0,255,255)

bezos = Turtle()
bezos.hideturtle()

def render(renderer, entities):
    renderer._tracer(1000000,0)
    renderer.clear()
    renderer.setundobuffer(None)
    renderer.pensize(scale)
    for i in entities:
        renderer.penup()
        pos = (i[0] * scale,i[1] * scale)
        renderer.setposition(pos)
        renderer.pendown()
        renderer.setposition(pos)

testArea = ((-1,-1),(-1,0),(0,-1),(-1,1),(1,-1),(0,1),(1,0),(1,1))

sphereOfInfluence = []
for i in testArea:
    sphereOfInfluence.append((-i[0],-i[1]))
sphereOfInfluence = tuple(sphereOfInfluence)

activeCells = [(0,1),(1,1),(-1,0),(0,0),(0,-1)]

renderPositions = set(activeCells)

for frame in range(500):

    Time = time.time()

    render(bezos,renderPositions)

    affectedCells = set()
    for cell in activeCells:
        for displacement in sphereOfInfluence:
            affectedCells.add((cell[0] + displacement[0],cell[1] + displacement[1]))

    newCells = []
    deadCells = []

    for cell in affectedCells:
        neighbors = 0
        for displacement in testArea:
            if (cell[0] + displacement[0],cell[1] + displacement[1]) in renderPositions:
                neighbors += 1
        if cell in renderPositions:
            if neighbors > 3 or neighbors < 2:
                deadCells.append(cell)
        if neighbors == 3:
                newCells.append(cell)

    for deadCell in deadCells:
        renderPositions.remove(deadCell)
    for newCell in newCells:
        renderPositions.add(newCell)

    activeCells = newCells + deadCells

    time.sleep(max(0,0.1 + Time - time.time()))
