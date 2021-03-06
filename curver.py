from dis import dis
import numpy as np



class Pather:
    def __init__(self,display_size) -> None:
        self.display_size = display_size

        self.target_1_pos = self.point_generate()
        self.target_2_pos = self.point_generate()
        self.weigth_ratio = 0
        self.weigth_inc = 0.02

    def point_generate(self):
        return np.random.randint(0,self.display_size[0],2)

    def point_distance(self,point1,point2):
        base = point1 - point2
        dist = np.sqrt(np.sum(np.power(base,2)))
        return dist

    def point_replace(self):
        self.target_1_pos = self.target_2_pos
        self.target_2_pos = self.point_generate()
        # while self.point_distance(self.target_1_pos,self.target_2_pos) < 300:
        #     self.target_2_pos = self.point_generate()

    def weigth_iterate(self):
        self.weigth_ratio += self.weigth_inc
        if self.weigth_ratio >= 1:
            self.point_replace()
            self.weigth_ratio = 0


    def point_eval(self,point):
        self.weigth_iterate()
        target = self.target_1_pos + np.subtract(self.target_2_pos,self.target_1_pos) * self.weigth_ratio
        return point + (target-point)/50, target


if __name__ =='__main__':
    a = Pather((800,400))


