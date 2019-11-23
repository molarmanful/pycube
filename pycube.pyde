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
    
    # CUBE.move(*"R U R' U'".split(r' '))
    
def draw():
    background(255)
    rotateX(-HALF_PI / 2)
    rotateY(HALF_PI / 2)
    CUBE.display()
