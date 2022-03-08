from curver import Pather
from pygamer import PyGamer
from pygame import Color, draw
from pygame import MOUSEBUTTONDOWN,MOUSEMOTION,KEYDOWN,KEYUP
from matrix import Matrix
import numpy as np

matrix_size = (100,100)
display_size = (1000,1000)

pp = PyGamer(display_size)
mm = Matrix(matrix_size,display_size,cursor_count=0)
cc = Pather(display_size)

cursor_pos = np.array([500,500])
color = np.random.random(3)

t = 0
key_pressing = False


def loop(p:PyGamer):

    global cursor_pos,t,color,weigth_inc

    t += 1
    if t % 60*4 == 0:
        color = np.random.random(3)

    mm.matrix_blur()
    mm.draw(p.surface)
    #mm.crisis()
    cursor_pos,target_mid = cc.point_eval(cursor_pos)
    target1,target2,weight = cc.target_1_pos.tolist(),cc.target_2_pos.tolist(),cc.weigth_ratio

    r1,r2 = 5 * weight,5 * (1-weight)
    # draw.circle(p.surface,Color(255,255,255),target1,r1)
    # draw.circle(p.surface,Color(255,255,255),target2,r2)
    draw.circle(p.surface,Color(255,0,255),target_mid.tolist(),3)



    mm.point_set(cursor_pos.tolist(),1,color.tolist())


def mouse_motion(p,event):
    button_left,_,button_right = event.buttons

    pos = event.pos
    #mm.point_set(pos,0.8,np.array([0.1,0.1,1]))

def key_down(p,event):
    pass
        



pp.callback_bind(MOUSEMOTION,mouse_motion)
pp.callback_bind(KEYDOWN,key_down)
pp.run(loop)