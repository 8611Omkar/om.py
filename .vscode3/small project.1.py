import  turtle
import math

pegasus =turtle.Turtle()
pegasus.getscreen().bgcolor("#994444")
pegasus.pendown()

for i in range(200):
    pegasus.forward(128)
    pegasus.left(216)
    pegasus.forward(360%2)
    pegasus.pensize(++i)

turtle.done()

