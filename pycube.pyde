add_library('peasycam')
from cube import Cube
from buffer import Buffer

COLORS = [
          color(255,   0,   0),
          color(255, 156,   0),
          color(255, 255,   0),
          color(255, 255, 255),
          color(  0,   0, 255),
          color(  0, 255,   0)
          ]


def setup():
    global CAM, BUF, BCAM, CUBE

    fullScreen(P3D)

    CAM = PeasyCam(this, 1000)
    CAM.setMinimumDistance(1000)
    CAM.setMaximumDistance(1000)
    CAM.setResetOnDoubleClick(False)
    CAM.setCenterDragHandler(None)
    CAM.setActive(False)

    BUF = Buffer(COLORS)
    BCAM = PeasyCam(this, BUF.buf, 1000)
    BCAM.setMinimumDistance(1000)
    BCAM.setMaximumDistance(1000)
    BCAM.setResetOnDoubleClick(False)
    BCAM.setCenterDragHandler(None)
    BCAM.setActive(False)

    CUBE = Cube(COLORS)


def draw():

    background(255)
    rotateX(-HALF_PI / 3)
    rotateY(HALF_PI * 2 / 3)
    CUBE.anim()
    CUBE.display()

    BUF.update()

    CAM.beginHUD()

    fill(0)
    textSize(20)
    textAlign(LEFT, TOP)
    text(['keyboard', 'mouse'][CUBE.mmode] + ' mode', 3, 3)

    CAM.endHUD()


def mousePressed():

    if CUBE.mmode and not CUBE.moving:
        p = BUF.getpixel()

        if p in COLORS:
            mod = "'" if mouseButton == RIGHT else ''
            CUBE.queue.add('FBUDLR'[COLORS.index(BUF.getpixel())] + mod)

def keyPressed():

    if key == ENTER:
        CAM.reset(300)
        BCAM.reset(300)
        CUBE.mmode = not CUBE.mmode
        CAM.setActive(CUBE.mmode)
        BCAM.setActive(CUBE.mmode)

    if not CUBE.mmode:

        if isinstance(key, basestring) and key.upper() in 'LMRUEDFSBXYZ':
            mod = "'" if key == key.upper() else ''
            CUBE.queue.add(key.upper() + mod)

        elif key == ' ' and not CUBE.moving:
            CUBE.scramble()
