import math
add_library('peasycam')
from cube import Cube

CUBE = Cube()

def setup():
    fullScreen(P3D)
    cam = PeasyCam(this, 1000)
    cam.setMinimumDistance(1000)
    cam.setMaximumDistance(1000)
    cam.setResetOnDoubleClick(False)
    cam.setCenterDragHandler(None)

    CUBE.move()
    
def draw():
    background(255)
    rotateX(-math.pi / 4)
    rotateY(math.pi / 4)
    CUBE.display()
