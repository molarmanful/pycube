"""A simulated Rubik's Cube with keyboard and mouse support.

Made by Ben Pang and Yusuf Jimoh for a final project. This code is
distributable under the MIT License. Makes use of the PeasyCam library
for camera-based dragging.

Todo:
    * Implement multiplayer networking.

"""

from __future__ import division
add_library('net')
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
SIZE = 100
SPEED = .3

try:
    import conf as conf
    if hasattr(conf, 'COLORS'): COLORS = conf.COLORS
    if hasattr(conf, 'SIZE'  ): SIZE = conf.SIZE
    if hasattr(conf, 'SPEED' ): SPEED = conf.SPEED
except:
    print('no conf.py found, falling back to defaults')

SHOWT = True


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
    CUBE = Cube(COLORS, SIZE, SPEED)


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
    textAlign(RIGHT, TOP)
    text('MODE: ' + ['keyboard', 'mouse'][CUBE.mmode], width - 3, 3)

    start = 3
    inc = 27
    times = CUBE.timer.times

    def trunc3(x):
        return int(x * 1000) / 1000

    def mn(xs):
        return min([x for x in xs if x != 'DNF'])

    def mx(xs):
        return max([x for x in xs if x != 'DNF'])

    def mean(xs):
        if 'DNF' in xs:
            return 'DNF'
        return trunc3(sum(xs) / len(xs))

    def best(f, n, xs):
        res = []
        for i in range(len(xs)):
            if(i + n < len(xs)):
                res.append(f(xs[i:i + n]))
        if all(x == 'DNF' for x in xs):
            return 'DNF'
        else:
            return min([x for x in res if x != 'DNF'])

    def avg(xs):
        ns = [float('inf') if x == 'DNF' else x for x in xs]
        ns.remove(min(ns))
        ns.remove(max(ns))
        if float('inf') in ns:
            return 'DNF'
        return trunc3(mean(ns))

    textAlign(LEFT, TOP)

    if SHOWT:

        if len(times) == 0:
            text('No times... yet.', 3, start)

        else:
            text('TIMES:', 3, start)
            for i in range(0, len(times), 5):
                start += inc
                text('  '.join(map(str, times[i:i + 5])), 3, start)

    else:

        text('# OF TIMES: ' + str(len(times)), 3, start)

        start += inc
        if len(times):
            start += inc
            text('SESSION BEST: ' + str(trunc3(mn(times))), 3, start)
            start += inc
            text('SESSION WORST: ' + str(trunc3(mx(times))), 3, start)
            start += inc
            text('SESSION MEAN: ' + str(mean(times)), 3, start)
        if len(times) > 2:
            start += inc
            text('SESSION AVG: ' + str(avg(times)), 3, start)

        start += inc
        if len(times) > 2:
            start += inc
            text('BEST mo3: ' + str(best(mean, 3, times)), 3, start)
        if len(times) > 4:
            start += inc
            text('BEST ao5: ' + str(best(avg, 5, times)), 3, start)
        if len(times) > 11:
            start += inc
            text('BEST ao12: ' + str(best(avg, 12, times)), 3, start)
        if len(times) > 99:
            start += inc
            text('BEST ao100: ' + str(best(avg, 100, times)), 3, start)

        start += inc
        if len(times) > 2:
            start += inc
            text('CURRENT bo3: ' + str(trunc3(mn(times[-3:]))), 3, start)
            start += inc
            text('CURRENT wo3: ' + str(trunc3(mx(times[-3:]))), 3, start)
            start += inc
            text('CURRENT mo3: ' + str(mean(times[-3:])), 3, start)

        start += inc
        if len(times) > 4:
            start += inc
            text('CURRENT bo5: ' + str(trunc3(mn(times[-5:]))), 3, start)
            start += inc
            text('CURRENT wo5: ' + str(trunc3(mx(times[-5:]))), 3, start)
            start += inc
            text('CURRENT ao5: ' + str(avg(times[-5:])), 3, start)

        start += inc
        if len(times) > 11:
            start += inc
            text('CURRENT bo12: ' + str(trunc3(mn(times[-5:]))), 3, start)
            start += inc
            text('CURRENT wo12: ' + str(trunc3(mx(times[-5:]))), 3, start)
            start += inc
            text('CURRENT ao12: ' + str(avg(times[-5:])), 3, start)

        start += inc
        if len(times) > 99:
            start += inc
            text('CURRENT bo100: ' + str(trunc3(mn(times[-100:]))), 3, start)
            start += inc
            text('CURRENT wo100: ' + str(trunc3(mx(times[-100:]))), 3, start)
            start += inc
            text('CURRENT ao100: ' + str(avg(times[-100:])), 3, start)

    if CUBE.disp:
        best = ''
        if CUBE.best():
            best = ' New personal best!'
        msg('You solved the cube!' + best)
    elif CUBE.solving:
        msg('Solving...')
    elif CUBE.scrambling:
        msg('Scrambling...')
    elif not CUBE.timing:
        msg('Press SPACE to begin a timed attempt')

    CAM.endHUD()


def stop():
    CUBE.file.write('\n'.join(map(str, CUBE.timer.times)))
    CUBE.file.close()


def msg(txt):

    textSize(30)
    textAlign(CENTER, TOP)
    text(txt, width / 2, 3)


def mousePressed():

    if CUBE.mmode and CUBE.free():
        # Use the buffer to find the proper face to move.
        p = BUF.getpixel(mouseX, mouseY)
        if p in COLORS:
            mod = "'" if mouseButton == RIGHT else ''
            CUBE.queue.add('FBUDLR'[COLORS.index(p)] + mod)

def keyPressed():

    global SHOWT

    if key == ENTER:
        # Switch between mouse and keyboard modes.
        CAM.reset(300)
        BCAM.reset(300)
        CUBE.mmode = not CUBE.mmode
        CAM.setActive(CUBE.mmode)
        BCAM.setActive(CUBE.mmode)

    elif key == 'q':
        link("https://bennyboy.tech/cubetut")

    elif key == '/':
        SHOWT = not SHOWT

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
