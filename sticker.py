class Sticker:
    
    def __init__(self, x, y, z, c, sz):
    
        self.x = x
        self.y = y
        self.z = z
        self.c = c
        self.sz = sz
        
        
    def display(self):
        
        x = self.x
        y = self.y
        z = self.z
        sz = self.sz
        
        pushMatrix()
        
        noStroke()
        fill(self.c)
        rectMode(CENTER)
        translate(x * sz / 2, y * sz / 2, z * sz / 2) 
        
        if x:
            rotateY(HALF_PI)
            
        elif y:
            rotateX(HALF_PI)
            
        square(0, 0, sz)
        
        popMatrix()
    
    
    def rX(self, a):
        
        y = round(self.y * cos(a) - self.z * sin(a))
        z = round(self.y * sin(a) + self.z * cos(a))
        self.y = y
        self.z = z
        
        
    def rY(self, a):
        
        x = round(self.x * cos(a) - self.z * sin(a))
        z = round(self.x * sin(a) + self.z * cos(a))
        self.x = x
        self.z = z
        
        
    def rZ(self, a):
        
        x = round(self.x * cos(a) - self.y * sin(a))
        y = round(self.x * sin(a) + self.y * cos(a))
        self.x = x
        self.y = y
