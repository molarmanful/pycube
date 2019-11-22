import math

class Piece:
    def __init__(self, x, y, z, sz):
        self.x = x
        self.y = y
        self.z = z
        self.sz = sz
        self.rx = 0
        self.ry = 0
        self.rz = 0
        
    def display(self):
        s = self.sz
        
        pushMatrix()
        stroke(0)
        strokeWeight(self.sz // 10 or 1)
        translate(self.x * s + s / 2, self.y * s + s / 2, self.z * s + s / 2)
        rotateX(self.rx * math.pi / 2)
        rotateY(self.ry * math.pi / 2)
        rotateZ(self.rz * math.pi / 2)
        translate(-s / 2, -s / 2, -s / 2)
        beginShape(QUADS)
    
        # F - red
        fill(255, 0, 0)
        vertex(0, 0, s)
        vertex(s, 0, s)
        vertex(s, s, s)
        vertex(0, s, s)
        # U - yellow
        fill(255, 255, 0)
        vertex(s, 0, s)
        vertex(s, 0, 0)
        vertex(0, 0, 0)
        vertex(0, 0, s)
        # R - green
        fill(0, 255, 0)
        vertex(s, 0, s)
        vertex(s, 0, 0)
        vertex(s, s, 0)
        vertex(s, s, s)
        # B - orange
        fill(255, 165, 0)
        vertex(s, 0, 0)
        vertex(0, 0, 0)
        vertex(0, s, 0)
        vertex(s, s, 0)
        # L - blue
        fill(0, 0, 255)
        vertex(0, 0, 0)
        vertex(0, 0, s)
        vertex(0, s, s)
        vertex(0, s, 0)
        # D - white
        fill(255, 255, 255)
        vertex(0, s, s)
        vertex(s, s, s)
        vertex(s, s, 0)
        vertex(0, s, 0)
    
        endShape()
        popMatrix()
        
    def pos(self, x=None, y=None, z=None):
        if x is not None: self.x = x
        if y is not None: self.y = y
        if z is not None: self.z = z
        
    def rot(self, rx=None, ry=None, rz=None):
        if rx is not None: self.rx = (self.rx + rx) % 4
        if ry is not None: self.ry = (self.ry + ry) % 4
        if rz is not None: self.rz = (self.rz + rz) % 4
