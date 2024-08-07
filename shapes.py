from turtle import Turtle
import random

t=Turtle()
colors=['red','green','blue','orange','brown','brown']

def shape(i):
    num_sides=i
    angle=360/num_sides
    for j in range(num_sides):
        t.forward(100)
        t.right(angle)

for i in range(3,11):
    t.color(random.choice(colors))
    shape(i)
