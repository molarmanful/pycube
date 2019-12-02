from sticker import Sticker

#this class contains all individual cube pieces and all its attributes
class Piece:
    
    def __init__(self, id, colors, x, y, z, sz):
        
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.sz = sz
        self.stickers = [
                         Sticker(-1,  0,  0, colors[0], self.sz),
                         Sticker( 1,  0,  0, colors[1], self.sz),
                         Sticker( 0, -1,  0, colors[2], self.sz),
                         Sticker( 0,  1,  0, colors[3], self.sz),
                         Sticker( 0,  0, -1, colors[4], self.sz),
                         Sticker( 0,  0,  1, colors[5], self.sz)
                         ]
        
        
    def display(self):
        
        sz = self.sz
        
        pushMatrix()
        
        stroke(0)
        strokeWeight(sz // 10 or 1)
        noFill()
        translate(sz * self.x, sz * self.y, sz * self.z)
        box(sz)
        
        for s in self.stickers:
            s.display()
            
        popMatrix()


    def pos(self, x, y, z): #this function is used to update the position of each cube 
        
        self.x = x
        self.y = y
        self.z = z
        
        
    def rX(self, dir): #rotate and translates cube pieces parallel to the x-axis 
        
        for s in self.stickers:
            s.rX(dir * HALF_PI)
        
        
    def rY(self, dir): #rotate and translates cube pieces parallel to the y-axis
        
        for s in self.stickers:
            s.rY(dir * HALF_PI)
        
        
    def rZ(self, dir): #rotate and translates cube pieces parallel to the z-axis
        
        for s in self.stickers:
            s.rZ(dir * HALF_PI)
