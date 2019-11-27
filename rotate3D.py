class rotate3D:
    def __init__(self,x_side,y_side,z_side,direction): 
        self.x_side = x_side
        self.y_side = y_side
        self.z_side = z_side
        self.rotationAngle = 0 
        self.speed = 0.01
        self.direction = direction
        self.rotating = False  
        self.rotationDone = False
        
    def moveAngle(self):
        if abs(self.rotationAngle) > HALF_PI: 
            self.rotationAngle = 0 
            self.rotating = False 
            self.rotationDone == True 
        elif (self.rotationAngle < HALF_PI) and (self.rotating == True):  
            self.rotationAngle += self.direction * self.speed 
        
        
