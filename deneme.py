import pygame
from pygame import Rect, display,color,QUIT,event,MOUSEMOTION,MOUSEBUTTONDOWN,MOUSEBUTTONUP,time,draw,KEYDOWN
import numpy as np

pygame.init()

matrix_shape = 100
display_size = 800
ratio = display_size/matrix_shape

class COLOR:
    BLACK = (0,0,0)
    BLUE = (0,0,255)


def matrix_reset(matrix):
    matrix = np.zeros((matrix_shape,matrix_shape))

def mapper(pos):
    x = (pos[0] * matrix_shape) // display_size 
    y = (pos[1] * matrix_shape) // display_size
    return x,y

def blur(matrix):
    kernel = np.array([0.15,0.7,0.15])
    matrix= np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 0, matrix)
    matrix= np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 1, matrix)
    return matrix

def matrix_random(matrix):
    pos = np.random.randint(0,matrix_shape,2)
    matrix[pos[0],pos[1]] = 1



matrix = np.zeros((matrix_shape,matrix_shape))
screen = display.set_mode((display_size,display_size))

matrix_random(matrix)

clock = time.Clock()
pressing = False
done = False
inc = 0.6
while not done:

    screen.fill(COLOR.BLACK)

    for ri,row in enumerate(matrix):
        for ci,col in enumerate(row):
            color_value = (0,0,col*255)
            draw.rect(screen,color_value,Rect(ci*ratio,ri*ratio,ratio,ratio))


    for ev in event.get():
        if ev.type == QUIT:
            done = True

        if ev.type == MOUSEBUTTONDOWN:
            pressing = True
        elif ev.type == MOUSEBUTTONUP:
            pressing = False
        elif ev.type == KEYDOWN:
            if ev.unicode == 'r':
                matrix_reset(matrix)


        if ev.type == pygame.MOUSEMOTION:
            pos = ev.pos
            button_left = ev.buttons[0]
            button_right = ev.buttons[2]
            if pressing:
                locs = list(map(mapper,[pos]))[0]
                if button_left:
                    curr = matrix[locs[1],locs[0]]
                    matrix[locs[1],locs[0]] = min(1,curr+inc)                
                elif button_right:
                    curr = matrix[locs[1],locs[0]]
                    matrix[locs[1],locs[0]] = max(0,curr-inc)
    matrix = blur(matrix)


    clock.tick(60)
    display.update()

pygame.quit()