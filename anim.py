class Anim:
    
    def __init__(self, x, y, z, dir, speed = .1): 
        self.x = x
        self.y = y
        self.z = z
        self.rot = 0
        self.speed = speed
        self.dir = dir
        self.roting = False  
        self.rotdone = False
    
    def start(self):
        self.roting = True
        while roting:
            self.step()
        
    def step(self):
        if abs(self.rot) > HALF_PI:
            self.rot = 0
            self.roting = False
            self.rotdone = True
        elif self.rot < HALF_PI and self.roting:  
            self.rot += self.dir * self.speed
        
        
