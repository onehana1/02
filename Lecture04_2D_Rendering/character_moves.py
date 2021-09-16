from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def right_move() :
    x=0
    while x<800:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
    
        x+=2
        delay(0.01)

def up_move() :
    y=90
    while y<600:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(800, y)
    
        y+=2
        delay(0.01)

def left_move() :
    x=800
    while x>0:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 600)
    
        x-=2
        delay(0.01)

def down_move() :
    y=600
    while y>90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(0, y)
    
        y-=2
        delay(0.01)


def radian(degree):
    return math.acos(-1)/180*degree


def circle_move():
    angle = 0
    
    while angle< 360:
        x = math.cos(angle) * 100 +500
        y = math.sin(angle) * 100 +300
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        angle += 20
        delay(0.01)


circle_move()


i=0
while 1:
    while i == 0 :
        right_move()
        up_move()
        left_move()
        down_move()
        i=1
        
    while i == 1 :
        circle_move()
        i=0


close_canvas()
