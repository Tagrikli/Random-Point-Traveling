from pygame import *


class PyGamer:
    def __init__(self,dimensions) -> None:
        self.surface = display.set_mode(dimensions,RESIZABLE)
        mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
        self.done = False
        self.clock = time.Clock()
        self.callbacks = []
        self.mouse_last_pos = (0,0)

    def callback_bind(self,event,callback):
        self.callbacks.append({'event':event,'callback':callback})

    def run(self,insider=None):

        while not self.done:
            self.surface.fill((0,0,0))
            for e in event.get():
                if e.type == QUIT:
                    self.done = True

                if e.type == MOUSEMOTION:
                    self.mouse_last_pos = e.pos

                for callback in self.callbacks:
                    if callback['event'] == e.type:
                        callback['callback'](self,e)

            
            insider and insider(self)


            display.update()
            self.clock.tick(120)