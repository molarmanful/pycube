import random
from piece import Piece
from anim import Anim


class Cube:
    
    def __init__(self, sz=100):
        self.sz = sz
        self.pieces = []
        self.queue = []
        self.mmode = False
        self.moving = 0
        
        id = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    self.pieces.append(Piece(id, x, y, z, self.sz))
                    id += 1
                    
                    
    def display(self):
        for p in self.pieces:
            p.display()
    
    
    def push(self, *ms):
        self.queue.extend(ms)
        
        
    def pop(self):
        return self.queue.pop()
    
        
    def scramble(self, l=25):
        for i in range(l):
            self.push(random.choice('LRUDFB') + random.choice(["'", '2']))
        self.move()
    
    def move(self, *ms): 
        mmap = {
                'L': (self.moveZ, -1, -1), 'M': (self.moveZ, 0, -1), 'R': (self.moveZ, 1,  1),
                'U': (self.moveY, -1,  1), 'E': (self.moveY, 0, -1), 'D': (self.moveY, 1, -1),
                'F': (self.moveX, -1, -1), 'S': (self.moveX, 0, -1), 'B': (self.moveX, 1,  1),
                'X': (self.moveZ,  2,  1), 'Y': (self.moveY, 2,  1), 'Z': (self.moveX, 2, -1)
                }
        
        if self.moving or len(self.queue):
            self.move(self.pop())
            self.move(*ms)
            
        else:
            for m in ms:
                f, slice, dir = mmap[m[0].upper()]
                if "'" in m:
                    f(slice, -dir)
                elif '2' in m:
                    f(slice, dir)
                    f(slice, dir)
                else:
                    f(slice, dir)
        
        
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
