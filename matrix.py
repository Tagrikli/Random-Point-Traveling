from cgi import print_arguments
from pygame import draw,Color
import numpy as np
import bezier
from scipy.signal import convolve2d
from curver import Curver



class Rect:
    def __init__(self,rect) -> None:
        self.poses = rect
        self.color = (0,0,200)

    def color_set(self,color):
        self.color = color

    def draw(self,surface):
        draw.rect(surface,self.color,self.poses)


class Matrix:
    def __init__(self,matrix_size,display_size,cursor_count = 1) -> None:
        self.matrix_size = matrix_size
        self.display_size = display_size
        self.ratio = self.display_size[0] /self.matrix_size[0]
        self.matrix = np.zeros((*matrix_size[::-1],3))
        self.blur_kernel = np.array([0.2495,0.50,0.2495])

        self.weight_scale = 40

        self.cursor_count = cursor_count
        self.cursor_colors = [[0.6,0.3,0.9],[0.8,0.7,0.4],[0,0,0],*[np.random.random(3) for _ in range(max(0,cursor_count-3))]]
        self.cursor_positions:list[list[int]] = [[int(self.display_size[0]*1/4),int(self.display_size[1]/4)] for _ in range(cursor_count)]

        self.cursor_curvers = [Curver() for _ in range(cursor_count)]



    def crisis(self):
        poses = []
        for curver in self.cursor_curvers:
            p = [curver.next_point()[0] * self.display_size[0],curver.next_point()[1] * self.display_size[1]]
            poses.append(p)    
        self.cursor_go(poses)

    def cursor_go(self,pos):
        for index,cursor_position in enumerate(self.cursor_positions):
            cursor_position[0] += int((pos[index][0] - cursor_position[0])) 
            cursor_position[1] += int((pos[index][1] - cursor_position[1])) 

    def cursors_draw(self):
        for index,cursor_position in enumerate(self.cursor_positions):
            self.point_set(cursor_position,0.8,np.array(self.cursor_colors[index]))

    def point_set(self,pos,increment,col):
        locs = list(map(self.position_mapper,[pos]))[0]
        curr = self.matrix[locs[1],locs[0]]
        self.matrix[locs[1],locs[0]] = (curr + col * increment).clip(0,1)  

    def matrix_blur(self):
        self.matrix= np.apply_along_axis(lambda x: np.convolve(x, self.blur_kernel, mode='same'), 0, self.matrix)
        self.matrix= np.apply_along_axis(lambda x: np.convolve(x, self.blur_kernel, mode='same'), 1, self.matrix)
        self.matrix.clip(0,1)



    def draw(self,surface):
        for ri,row in enumerate(self.matrix):
            for ci,col in enumerate(row):
                cv = (col[0]*255,col[1]*255,col[2]*255)
                
                draw.rect(surface,cv,(ci*self.ratio,ri*self.ratio,self.ratio,self.ratio))
        self.cursors_draw()    

    def position_mapper(self,pos):
        x = int((pos[0] * self.matrix_size[0]) / self.display_size[0]) 
        y = int((pos[1] * self.matrix_size[1]) / self.display_size[1])
        return x,y
