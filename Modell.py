import pygame as pg
import numpy as np


class cell:
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        
    

class GOL:
    def __init__(self,lengde = 400 ,bredde = 400):
        pg.init()
        self.lengde = lengde
        self.bredde = bredde
        self.skjerm = pg.display.set_mode((self.lengde,self.bredde))
        self.skjerm.fill((255,245,255))
        self.runnin = True
        
    def run(self):
        
        while self.runnin:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.runnin = False
                pg.display.flip()
        pg.quit()
        
game = GOL()
game.run()



        
    

        


        
        
        
