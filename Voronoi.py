import random
from turtle import *

space = Screen()
space.setup(width=800, height=800, startx=None, starty=None)
space.colormode(255)

bezos = Turtle()
bezos.speed(0)
bezos.hideturtle()
bezos.setundobuffer(None)
bezos._tracer(1000000,0)

def render(entities, color, pensize):
    bezos.pencolor(color)
    bezos.pensize(pensize)
    for i in range(len(entities)):
        for j in range(len(entities[i][1])):
            bezos.penup()
            bezos.goto(entities[i][0])
            bezos.pendown()
            bezos.goto(entities[i][1][j])

def rp(entities, color, pensize):
    bezos.pencolor(color)
    bezos.pensize(pensize)
    for i in entities:
        bezos.penup()
        bezos.goto(i)
        bezos.pendown()
        bezos.goto(i)

X = 0
Y = 1

points = set()
width = 864
height = 864
for i in range(100):
    points.add((random.random() * 2 * width - width,random.random() * 2 * height - height))
points = list(points)

def intersection(A,B,C):
    point = ((A[X] + B[X]) / 2, (A[Y] + B[Y]) / 2)
    m = -(A[X] - B[X]) / (A[Y] - B[Y])
    b = point[Y] - m * point[X]
    point2 = ((A[X] + C[X]) / 2, (A[Y] + C[Y]) / 2)
    m2 = -(A[X] - C[X]) / (A[Y] - C[Y])
    b2 = point2[Y] - m2 * point2[X]
    x = (b2 - b)/(m - m2)
    y = m * x + b
    return (x,y)

validTriangles = []
for i in range(len(points)):
    for j in range(i+1,len(points)):
        for k in range(j+1,len(points)):
            point = intersection(points[i],points[j],points[k])
            distance = (point[X] - points[i][X])**2 + (point[Y] - points[i][Y])**2
            valid = True
            for l in range(len(points)):
                if l == k or l == j or l == i:
                    continue
                if (point[X] - points[l][X])**2 + (point[Y] - points[l][Y])**2 < distance:
                    valid = False
                    break
            if valid:
                validTriangles.append((points[i],points[j],points[k],point))

nodes = []
for i in range(len(validTriangles)):
    nodes.append([validTriangles[i][3],[]])
    for j in range(len(validTriangles)):
        if i == j:
            continue
        sharedPoints = 0
        if validTriangles[j][0] == validTriangles[i][0] or validTriangles[j][0] == validTriangles[i][1] or validTriangles[j][0] == validTriangles[i][2]:
            sharedPoints += 1
        if validTriangles[j][1] == validTriangles[i][0] or validTriangles[j][1] == validTriangles[i][1] or validTriangles[j][1] == validTriangles[i][2]:
            sharedPoints += 1
            if sharedPoints == 2:
                nodes[i][1].append(validTriangles[j][3])
                continue
        if validTriangles[j][2] == validTriangles[i][0] or validTriangles[j][2] == validTriangles[i][1] or validTriangles[j][2] == validTriangles[i][2]:
            sharedPoints += 1
        if sharedPoints == 2:
            nodes[i][1].append(validTriangles[j][3])
        if len(nodes[-1][1]) == 3:
            break

rp(points, "red", 5)
render(nodes, "black", 1)

bezos.penup()
bezos.goto(0,0)
space.exitonclick()
