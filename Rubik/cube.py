from piece import Piece

class Cube:
    def __init__(self, sz=100):
        self.sz = sz
        self.pieces = {}
        
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    self.pieces[x, y, z] = Piece(x, y, z, self.sz)
                    
    def display(self):
        pushMatrix()
        translate(-self.sz * 3 / 2, -self.sz * 3 / 2, -self.sz * 3 / 2)
        for c in self.pieces:
            self.pieces[c].display()
        popMatrix()
        
    def move(self): 
        for c in self.pieces:
            if c[0] == 0:
                self.pieces[c].rot(rx=1)
                
        self.pieces[0, 0, 0].pos(y=2)
        self.pieces[0, 2, 0].pos(z=2)
        self.pieces[0, 2, 2].pos(y=0)
        self.pieces[0, 0, 2].pos(z=0)
        
        self.pieces[0, 1, 0].pos(y=2, z=1)
        self.pieces[0, 2, 1].pos(y=1, z=2)
        self.pieces[0, 1, 2].pos(y=0, z=1)
        self.pieces[0, 0, 1].pos(y=1, z=0)
