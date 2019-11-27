add_library('peasycam')
from cube import Cube

CUBE = Cube()
CAM = None


def setup():
    global CAM
    
    fullScreen(P3D)
    
    CAM = PeasyCam(this, 1000)
    CAM.setMinimumDistance(1000)
    CAM.setMaximumDistance(1000)
    CAM.setResetOnDoubleClick(False)
    CAM.setCenterDragHandler(None)
    CAM.setActive(False)
    
    
def draw():
    
    background(255)
    rotateX(-HALF_PI / 3)
    rotateY(HALF_PI * 2 / 3)
    CUBE.anim()
    CUBE.display()
    
    CAM.beginHUD()
    
    fill(0)
    textSize(20)
    textAlign(LEFT, TOP)
    text(['keyboard', 'mouse'][CUBE.mmode] + ' mode', 3, 3)
    
    CAM.endHUD()


def keyPressed():
    
    if key == ENTER:
        CAM.reset(300)
        CUBE.mmode = not CUBE.mmode
        CAM.setActive(CUBE.mmode)
        
    if not CUBE.mmode:
            
        if isinstance(key, basestring) and key.upper() in 'LMRUEDFSBXYZ':
            mod = "'" if key == key.upper() else ''
            CUBE.queue.add(key.upper() + mod)
        
        elif key == ' ' and not CUBE.moving:
            CUBE.scramble()
