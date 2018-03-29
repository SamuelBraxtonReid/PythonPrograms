import random
from turtle import *

space = Screen()
space.colormode(255)
space.bgcolor(0,0,0)

bezos = Turtle()
bezos.hideturtle()
bezos.pencolor((255,255,255))

scale = 5

bezos.pensize(scale)

def render(renderer, entities):
    renderer._tracer(1000000,0)
    renderer.clear()
    renderer.setundobuffer(None)
    while len(entities) > 0:

        entity = next(iter(entities))
        ox = entity[0]
        oy = entity[1]

        xpos = ox
        while (xpos-1, oy) in entities:
            xpos -= 1
        startx = xpos
        while (xpos+1, oy) in entities:
            xpos += 1
        endx = xpos

        ypos = oy
        while (ox, ypos-1) in entities:
            ypos -= 1
        starty = ypos
        while (ox, ypos+1) in entities:
            ypos += 1
        endy = ypos

        if endx - startx < endy - starty:
            for i in range(starty, endy+1):
                entities.remove((ox,i))
            ox *= scale
            bezos.penup()
            bezos.goto(ox,starty*scale)
            bezos.pendown()
            bezos.goto(ox,endy*scale)
        else:
            for i in range(startx, endx+1):
                entities.remove((i,oy))
            oy *= scale
            bezos.penup()
            bezos.goto(startx*scale,oy)
            bezos.pendown()
            bezos.goto(endx*scale,oy)


testArea = ((-1,-1),(-1,0),(0,-1),(-1,1),(1,-1),(0,1),(1,0),(1,1))

cells = set()
rad = 40
for i in range(2 * rad * rad):
    randx = random.randint(-rad,rad)
    randy = random.randint(-rad,rad)
    if randx**2 + randy**2 > rad**2:
        continue
    cells.add((randx,randy))
newCells = list(cells)

deadCells = []

positions = {}
for i in newCells:
    positions[i] = [1,0]

renderPositions = set()

for frame in range(1000):

    renderPositions.clear()
    for i in positions.keys():
        if positions[i][0] == 1:
            renderPositions.add(i)
    render(bezos,renderPositions)

    for newCell in newCells:
        for displacement in testArea:
            cell = (newCell[0]+displacement[0],newCell[1]+displacement[1])
            if cell in positions:
                positions[cell][1] += 1
            else:
                positions[cell] = [-2,1]

    for deadCell in deadCells:
        for displacement in testArea:
            cell = (deadCell[0]+displacement[0],deadCell[1]+displacement[1])
            if positions[cell][1] == 1 and positions[cell][0] == -2:
                del positions[cell]
                continue
            positions[cell][1] -= 1
        if positions[deadCell][1] == 0:
            del positions[deadCell]
            continue
        positions[deadCell][0] = -2

    newCells = []
    deadCells = []

    for position in positions:
        if positions[position][0] == 1:
            if positions[position][1] > 3 or positions[position][1] < 2:
                positions[position][0] = -1
                deadCells.append(position)
        elif positions[position][1] == 3:
            positions[position][0] = 1
            newCells.append(position)

bezos.penup()
bezos.goto(0,0)
