"""A simulated Rubik's Cube with keyboard and mouse support.

Made by Ben Pang and Yusuf Jimoh for a final project. This code is
distributable under the MIT License. Makes use of the PeasyCam library
for camera-based dragging.

Todo:
    * Implement timing mechanisms.
    * Finish UI.
    * Implement multiplayer networking.

"""

add_library('peasycam')
from cube import Cube
from buffer import Buffer

# Color order is FBUDLR.
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

    # Initialize the camera.
    CAM = PeasyCam(this, 1000)
    CAM.setMinimumDistance(1000)
    CAM.setMaximumDistance(1000)
    CAM.setResetOnDoubleClick(False)
    CAM.setCenterDragHandler(None)
    CAM.setActive(False)

    # Initialize the buffer.
    BUF = Buffer(COLORS)

    # Initialize an offscreen camera for the buffer.
    BCAM = PeasyCam(this, BUF.buf, 1000)
    BCAM.setMinimumDistance(1000)
    BCAM.setMaximumDistance(1000)
    BCAM.setResetOnDoubleClick(False)
    BCAM.setCenterDragHandler(None)
    BCAM.setActive(False)

    # Initialize the cube.
    CUBE = Cube(COLORS)


def draw():

    background(255)
    rotateX(-HALF_PI / 3)
    rotateY(HALF_PI * 2 / 3)


    # Update both cube and buffer.
    CUBE.anim()
    CUBE.display()
    BUF.update()
    
    

    CAM.beginHUD()

    fill(0)
    textSize(20)
    textAlign(LEFT, TOP)
    text('MODE: ' + ['keyboard', 'mouse'][CUBE.mmode], 3, 3)
    text('TIMES: ' + ', '.join(map(str, CUBE.timer.times)), 3, 30)

    CAM.endHUD() 
    
    if CUBE.dispm1: 
        message(1)  
    elif CUBE.dispm2:  
        message(2) 


def stop():
    CUBE.timefile.to_file() 
    
def message(mesg): 
    if mesg == 1:
        CAM.beginHUD() 
        fill(0)
        textSize(30)
        textAlign(RIGHT, TOP) 
        text("You solved the cube!", (6*width)/10, 10)
        CAM.endHUD() 
    else:
        CAM.beginHUD() 
        fill(0)
        textSize(30) 
        textAlign(RIGHT, TOP)
        text("You solved the cube! Best Time!!", (6*width)/10, 10)  
        CAM.endHUD() 
        
def mousePressed():

    if CUBE.mmode and CUBE.free():
        # Use the buffer to find the proper face to move.
        p = BUF.getpixel(mouseX, mouseY)
        if p in COLORS:
            mod = "'" if mouseButton == RIGHT else ''
            CUBE.queue.add('FBUDLR'[COLORS.index(p)] + mod)

def keyPressed():

    if key == ENTER:
        # Switch between mouse and keyboard modes.
        CAM.reset(300)
        BCAM.reset(300)
        CUBE.mmode = not CUBE.mmode
        CAM.setActive(CUBE.mmode)
        BCAM.setActive(CUBE.mmode)

    elif CUBE.free():

        if key == TAB:
            # Press TAB to auto-solve the cube.
            if CUBE.timing:
                # Disqualify any timings if auto-solve runs.
                if CUBE.timer.ing:
                    CUBE.timer.times[-1] = 'DNF'
                else:
                    CUBE.timer.times.append('DNF')
                CUBE.timer.end()
                CUBE.timing = False

            CUBE.solve()

        elif key == ' ' and not CUBE.timing:
            # Press SPACEBAR to begin a time attempt.
            CUBE.time() 

    if not CUBE.mmode:
        if isinstance(key, basestring) and key.upper() in 'LMRUEDFSBXYZ':
            # Execute moves based on keys (SHIFT reverses direction).
            mod = "'" if key == key.upper() else ''
            CUBE.queue.add(key.upper() + mod)
