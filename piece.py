from sticker import Sticker


class Piece:
    
    def __init__(self, id, x, y, z, sz):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.sz = sz
        self.stickers = [
                         Sticker(-1, 0, 0, color(255, 0, 0), self.sz),
                         Sticker(1, 0, 0, color(255, 156, 0), self.sz),
                         Sticker(0, -1, 0, color(255, 255, 0), self.sz),
                         Sticker(0, 1, 0, color(255, 255, 255), self.sz),
                         Sticker(0, 0, -1, color(0, 0, 255), self.sz),
                         Sticker(0, 0, 1, color(0, 255, 0), self.sz)
                         ]
        
        
    def display(self):
        x = self.x
        y = self.y
        z = self.z
        sz = self.sz
        
        pushMatrix()
        stroke(0)
        strokeWeight(sz // 10 or 1)
        noFill()
        translate(sz * (x + .5), sz * (y + .5), sz * (z + .5))
        box(sz)
        for s in self.stickers:
            s.display()
        popMatrix()


    def pos(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
        
    def rX(self, dir):
        for s in self.stickers:
            s.rX(dir * HALF_PI)
        
        
    def rY(self, dir):
        for s in self.stickers:
            s.rY(dir * HALF_PI)
        
        
    def rZ(self, dir):
        for s in self.stickers:
            s.rZ(dir * HALF_PI)
