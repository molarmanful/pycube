class Buffer:
    
    def __init__(self, colors, sz = 100):
        
        self.colors = colors
        self.sz = 100
        self.buf = createGraphics(width, height, P3D)
        
    
    def update(self):
        
        colors = self.colors
        sz = self.sz
        buf = self.buf
        
        buf.beginDraw()
        
        buf.background(0)
        buf.rotateX(-HALF_PI / 3)
        buf.rotateY(HALF_PI * 2 / 3)
        
        faces = [
                 (-1,  0,  0, colors[0]),
                 ( 1,  0,  0, colors[1]),
                 ( 0, -1,  0, colors[2]),
                 ( 0,  1,  0, colors[3]),
                 ( 0,  0, -1, colors[4]),
                 ( 0,  0,  1, colors[5])
                 ]
        
        for x, y, z, c in faces:
            
            buf.pushMatrix()
            
            buf.noStroke()
            buf.fill(c)
            buf.rectMode(CENTER)
            buf.translate(x * sz * 1.5, y * sz * 1.5, z * sz * 1.5)
        
            if x:
                buf.rotateY(HALF_PI)
                
            elif y:
                buf.rotateX(HALF_PI)
                
            buf.square(0, 0, sz * 3)
            
            buf.popMatrix()
            
        buf.endDraw()
        
    def getpixel(self):
        self.buf.loadPixels()
        return self.buf.pixels[mouseY * width + mouseX]
