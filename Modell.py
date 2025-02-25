class cell:
    def __init__(self,posx,posy,lengde,bredde):
        self.posx = posx
        self.posy = posy
    def oppdater_celle_life(self,next_state):
        self.alive = next_state
    

class GOL:
    def __init__(self):
        pass

    def oppdater(self):
        next_states = []
        for row in self.cells:
            next_states.append([cell.getNextState() for cell in row])
        for x, y in zip(self.width, self.height):
            self.cell[x],[y].oppdater_celle_life(next_states[x],[y])

