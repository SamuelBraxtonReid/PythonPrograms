from turtle import *

scale = 5

space = Screen()
space.colormode(255)
space.bgcolor(255,255,255)

bezos = Turtle()
bezos.hideturtle()

def render(renderer, entities):
    renderer._tracer(1000000,0)
    renderer.clear()
    renderer.setundobuffer(None)
    renderer.pensize(scale)
    for i in entities.keys():
        if entities[i][0] == 1:
            pos = (i[0]*scale,i[1]*scale)
            renderer.penup()
            renderer.setposition(pos)
            renderer.pendown()
            renderer.setposition(pos)

import random

testArea = ((-1,-1),(-1,0),(0,-1),(-1,1),(1,-1),(0,1),(1,0),(1,1))

cells = set()
for i in range(512):
    cells.add((random.randint(-20,20),random.randint(-20,20)))
newCells = list(cells)

deadCells = []

positions = {}
for i in newCells:
    positions[i] = [1,0]

for frame in range(1000):

    render(bezos,positions)

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

    for position in positions.keys():
        if positions[position][0] == 1:
            if positions[position][1] > 3 or positions[position][1] < 2:
                positions[position][0] = -1
                deadCells.append(position)
        elif positions[position][1] == 3:
            positions[position][0] = 1
            newCells.append(position)
