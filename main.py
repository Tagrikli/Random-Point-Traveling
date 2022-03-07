from curver import Pather
from pygamer import PyGamer
from pygame import Color, draw,MOUSEBUTTONDOWN,MOUSEMOTION
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
def loop(p:PyGamer):

    global cursor_pos,t,color

    t += 1
    if t % 60*4 == 0:
        color = np.random.random(3)

    mm.matrix_blur()
    mm.draw(p.surface)
    #mm.crisis()
    cursor_pos = cc.point_eval(cursor_pos)

    mm.point_set(cursor_pos.tolist(),1,color.tolist())


def mouse_motion(p,event):
    button_left,_,button_right = event.buttons

    pos = event.pos
    #mm.point_set(pos,0.8,np.array([0.1,0.1,1]))





pp.callback_bind(MOUSEMOTION,mouse_motion)
pp.run(loop)