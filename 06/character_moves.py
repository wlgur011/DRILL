from pico2d import *
import math
import os

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


x = 400
y = 90
def redraw(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)

def move_rect(x,y):
    while(x<800):
        x=x+4
        redraw(x,y)
    while(y<550):
        y=y+4
        redraw(x,y)
    while(x>0):
        x=x-4
        redraw(x,y)
    while(y>90):
        y=y-4
        redraw(x,y)
    while(x<400):
        x=x+4
        redraw(x,y)

def move_ellipse(x,y, r = 240):
    k=0
    while(k<360*math.pi/180):
        x=400+math.sin(k)*r
        y=330-math.cos(k)*r
        k=k+0.05
        redraw(x,y)
    
while(1):
    move_rect(x,y)
    move_ellipse(x,y)
    
    
close_canvas()
