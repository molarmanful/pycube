from piece import Piece


class Cube:
    
    def __init__(self, sz=100):
        self.sz = sz
        self.pieces = []
        id = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    self.pieces.append(Piece(id, x, y, z, self.sz))
                    id += 1
                    
                    
    def display(self):
        pushMatrix()
        translate(-self.sz * .5, -self.sz * .5, -self.sz * .5)
        for p in self.pieces:
            p.display()
        popMatrix()
    
    
    def move(self, *ms):
        mmap = {
                'L': (self.moveZ, -1), 'M': (self.moveZ, 0), 'R': (self.moveZ, 1),
                'U': (self.moveY, -1), 'E': (self.moveY, 0), 'D': (self.moveY, 1),
                'F': (self.moveY, -1), 'S': (self.moveY, 0), 'B': (self.moveY, 1),
                'X': (self.moveX,  2), 'Y': (self.moveY, 2), 'Z': (self.moveZ, 2)
                }
        
        for m in ms:
            f, slice = mmap[m[0].upper()]
            f(slice, -1 if m[-1] == "'" else 1)
        
        
    def moveX(self, slice, dir=1):
        for p in self.pieces:
            if slice > 1 or p.x == slice:
                t = PMatrix2D()
                t.rotate(dir * HALF_PI)
                t.translate(p.y, p.z)
                p.rX(dir)
                p.pos(round(p.x), round(t.m02), round(t.m12))
    
    
    def moveY(self, slice, dir=1):
        for p in self.pieces:
            if slice > 1 or p.y == slice:
                t = PMatrix2D()
                t.rotate(dir * HALF_PI)
                t.translate(p.x, p.z)
                p.rY(dir)
                p.pos(round(t.m02), round(p.y), round(t.m12))
    
    
    def moveZ(self, slice, dir=1):
        for p in self.pieces:
            if slice > 1 or p.z == slice:
                t = PMatrix2D()
                t.rotate(dir * HALF_PI)
                t.translate(p.x, p.y)
                p.rZ(dir)
                p.pos(round(t.m02), round(t.m12), round(p.z))
