from turtle import *

wn = Screen()
wn.setup(500,500)
turtle = Turtle()
turtle.speed("fastest")

step = 31
'''
def draw_square(length,angle):
    for i in range (0,step):
        for b in range (0,4):
            turtle.forward(length+i)
            turtle.right(angle+b)
'''

def draw_square(length,angle):
    global step
    if step<1:
        return 
    else:
        turtle.forward(length)
        turtle.right(angle)
        if angle-90==3:
            step=step-1
            angle=89
            length=length+1
        return draw_square(length,angle+1)
   
draw_square(100,90)
                                            
