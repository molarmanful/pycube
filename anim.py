class Anim:
    
    def __init__(self, cube, axis, slice, dir, speed=.3):   
        
        self.cube = cube
        self.axis = axis
        self.slice = slice
        self.dir = dir
        self.rot = 0
        self.speed = speed
        self.ing = True
        self.done = False
        
        
    def step(self): #defines each move of the cube 
        
        if self.ing:
            self.rot += self.dir * self.speed
            self.cube.moving = True
            
            if abs(self.rot) > HALF_PI: #restricts rotation to 90 degrees 
                self.rot = 0
                self.ing = False
                self.done = True
                self.cube.moving = False
                
                #check for turn axis and rotate cube as necessary
                if self.axis == 2:
                    self.cube.moveZ(self.slice, self.dir) 
                    
                elif self.axis == 1:
                    self.cube.moveY(self.slice, -self.dir)
                    
                else:
                    self.cube.moveX(self.slice, self.dir)
