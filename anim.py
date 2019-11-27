class Anim:
    
    def __init__(self, cube, axis, slice, dir, speed=.2):
        
        self.cube = cube
        self.axis = axis
        self.slice = slice
        self.dir = dir
        self.rot = 0
        self.speed = speed
        self.ing = True
        self.done = False
        
        
    def step(self):
        
        if self.ing:
            self.rot += self.dir * self.speed
            
            if abs(self.rot) > HALF_PI:
                self.rot = 0
                self.ing = False
                self.done = True
                
                if self.axis == 2:
                    self.cube.moveZ(self.slice, self.dir)
                    
                elif self.axis == 1:
                    self.cube.moveY(self.slice, -self.dir)
                    
                else:
                    self.cube.moveX(self.slice, self.dir)
