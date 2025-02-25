import pygame as pg
import numpy as np


class cell:
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
    def oppdater_celle_life(self,next_state):
        self.alive = next_state
#endring
    

class GOL:
    def __init__(self,lengde = 400 ,bredde = 400, celle = 10):
        pg.init()
        self.lengde = lengde
        self.bredde = bredde
        self.skjerm = pg.display.set_mode((self.lengde,self.bredde))
        self.skjerm.fill((144,245,144))
        self.celle = celle
        self.rader = self.bredde // self.celle
        self.kolonner = self.lengde // self.celle
        
        #lager ruter med verdier fra 0 til 1, om de lever eller ikke
        self.ruter = np.random.choice([0,1], size=(self.rader, self.kolonner))
        self.runnin = True
        
    def oppdater(self):
        next_states = []
        for row in self.cells:
            next_states.append([cell.getNextState() for cell in row])
        for x, y in zip(self.width, self.height):
            self.cell[x],[y].oppdater_celle_life(next_states[x],[y])
        
    def Celler(self):
        for i in range(self.rader):
            for u in range(self.kolonner):
                if self.ruter[i,u] == 1:
                    pg.draw.rect(self.skjerm,(0,0,0),(u*self.celle, i*self.celle, self.celle-1, self.celle-1),)

    def run(self):
        self.Celler()
        while self.runnin:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.runnin = False
                pg.display.flip()
        pg.quit()
        
game = GOL()
game.run()



        
    

        


        
        
        
