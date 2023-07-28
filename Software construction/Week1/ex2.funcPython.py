from turtle import *

def build_SquareWall(turtle,size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90) # reset arrow

def build_Roof(turtle,size):
    turtle.left(60)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(180) # reset arrow

def build_House(turtle,size):
    build_SquareWall(turtle,size)
    build_Roof(turtle,size)

tt = Turtle()
build_House(tt,300)

