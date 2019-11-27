import random
from piece import Piece
from anim import Anim
from stack import Stack


class Cube:
    
    def __init__(self, sz=100, speed=.2):
        
        self.sz = sz
        self.speed = speed
        self.pieces = []
        self.queue = Stack()
        self.anims = Stack()
        self.mmode = False
        self.moving = False
        
        id = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    self.pieces.append(Piece(id, x, y, z, self.sz))
                    id += 1
                    
                    
    def display(self):
        
        a = self.anims.get(0)
        for p in self.pieces:
            pushMatrix()
            
            if a:
                if a.axis == 2 and p.z == a.slice:
                    rotateZ(a.rot)
                    
                elif a.axis == 1 and p.y == a.slice:
                    rotateY(a.rot)
                    
                elif a.axis == 0 and p.x == a.slice:
                    rotateX(a.rot)
                    
            p.display()
            popMatrix()
    
        
    def scramble(self, l=25):
        
        for i in range(l):
            self.queue.add(random.choice('LRUDFB') + random.choice(["'", '2']))
    
    def move(self, *ms):
        
        mmap = {
                'L': (2, -1, -1), 'M': (2, 0, -1), 'R': (2, 1,  1),
                'U': (1, -1, -1), 'E': (1, 0,  1), 'D': (1, 1,  1),
                'F': (0, -1, -1), 'S': (0, 0, -1), 'B': (0, 1,  1),
                'X': (2,  2,  1), 'Y': (1, 2,  1), 'Z': (0, 2, -1)
                }
        
        for m in ms:
            axis, slice, dir = mmap[m[0].upper()]
            
            if "'" in m:
                self.anims.add(Anim(self, axis, slice, -dir, self.speed))
                
            elif '2' in m:
                self.anims.add(Anim(self, axis, slice, dir, self.speed), Anim(self, axis, slice, dir, self.speed))
                
            else:
                self.anims.add(Anim(self, axis, slice, dir, self.speed))
        
        
    def anim(self):
        
        if self.anims.get(0):
            if self.anims.get(0).done:
                self.anims.pop()
                
            else:
                self.anims.get(0).step()
                
        elif self.queue.get(0):
            self.move(self.queue.pop())
        
        
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
