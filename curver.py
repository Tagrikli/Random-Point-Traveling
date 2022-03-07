from dis import dis
import bezier
import numpy as np



class Pather:
    def __init__(self,display_size) -> None:
        self.display_size = display_size

        self.target_1_pos = self.point_generate()
        self.target_2_pos = self.point_generate()
        self.weigth_ratio = 0
        self.weigth_inc = 0.1

    def point_generate(self):
        return np.random.randint(0,self.display_size[0],2)

    def point_replace(self):
        self.target_1_pos = self.target_2_pos
        self.target_2_pos = self.point_generate()
        # while np.linalg.norm(self.target_2_pos - self.target_1_pos) > 300:
        #     self.target_2_pos = self.point_generate()

    def weigth_iterate(self):
        self.weigth_ratio += self.weigth_inc
        if self.weigth_ratio >= 1:
            self.point_replace()
            self.weigth_ratio = 0


    def point_eval(self,point):
        self.weigth_iterate()
        target = self.target_1_pos + np.subtract(self.target_2_pos,self.target_1_pos) * self.weigth_ratio
        return point + (target-point)/30


class Curver:
    def __init__(self) -> None:
        
        self.t = np.random.random()
        self.point_count = 4
        self.points = np.random.random((self.point_count,2))

        self.curve = bezier.Curve(self.points.T,self.point_count-1)

    def next_point(self):
        self.t += 0.003
        if self.t >= 1:
            self.t = 0.0

            self.points = np.concatenate((self.points[-1:],np.random.random((self.point_count-1,2))))

            self.curve = bezier.Curve(self.points.T,self.point_count-1)
    

        return self.curve.evaluate(self.t).T[0]

if __name__ =='__main__':
    a = Pather((800,400))


