import random
from piece import Piece
from anim import Anim
from stack import Stack


class Cube:
    """Handles rendering and updating of the cube.

    Args:
        colors (:list:`int`): Color scheme in `FBUDLR` order.
        sz (int): Size of each cube piece (default 100).
        speed (int): Animation speed in radians per frame (default .3).

    Attributes:
        colors (:list:`int`): Color scheme in `FBUDLR` order.
        sz (int): Size of each cube piece (default 100).
        speed (int): Animation speed in radians per frame (default .3).
        pieces (:list:`Piece`): Container for all cube pieces.
        queue (:Stack:`str`): Queue for moves that need to be executed.
        anims (:Stack:`Anim`): Queue for animations that need to be run.
        mmode (bool): Whether mouse mode is on.
        moving (bool): Whether the cube is currently animating.

    """

    def __init__(self, colors, sz=100, speed=.3):
        self.colors = colors
        self.sz = sz
        self.speed = speed
        self.pieces = []
        self.queue = Stack()
        self.anims = Stack()
        self.mmode = True
        self.moving = False

        id = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if (x, y, z) != (0, 0, 0): # Remove the core piece.
                        # Add pieces to pieces.
                        self.pieces.append(Piece(id, colors, x, y, z, self.sz))
                        id += 1


    def display(self):
        """Displays the cube.

        This method is called during each `draw` call (see
        `pycube.pyde`).
        """

        a = self.anims.get(0)
        for p in self.pieces:
            pushMatrix()

            if a:
                # Rotate slices to show current animation progress.
                if a.axis == 2 and (a.slice > 1 or p.z == a.slice):
                    rotateZ(a.rot)
                elif a.axis == 1 and (a.slice > 1 or p.y == a.slice):
                    rotateY(a.rot)
                elif a.axis == 0 and (a.slice > 1 or p.x == a.slice):
                    rotateX(a.rot)

            p.display()
            popMatrix()


    def getpiece(self, x, y, z):
        """Finds the piece with the given (x,y,z) coordinates.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            z (int): The z-coordinate.

        Returns:
            Piece: The found piece, or None if no piece matches the query.

        """

        for p in self.pieces:
            if (p.x, p.y, p.z) == (x, y, z):
                return p


    def solved(self):
        """Checks if the cube is solved.

        Returns:
            bool: True if solved, False otherwise.

        """

        for p in self.pieces:
            if [p.x, p.y, p.z].count(0) < 2: # Filter out centers.
                # Compare each sticker color with its respective center.
                for i, s in enumerate(p.stickers):
                    cen = self.getpiece(s.x, s.y, s.z).getsticker(s.x, s.y, s.z)
                    if s.c != cen.c:
                        return False

        return True


    def scramble(self, l=25):

        a = ' '
        b = ' '

        for i in range(l):
            choices = ['RL', 'UD', 'FB']

            for i, m in enumerate(choices):
                if a in m:
                    choices[i] = m.replace(a, '')
                    if b in m:
                        choices[i] = ''

            b, a = a, random.choice(''.join(choices))
            self.queue.push(a + random.choice(["'", '2', '']))


    def move(self, *ms):
        #mmap is a dictionary that contains all the possible cube movememnts and the parameters needed to rotate each cube successfully
        mmap = {
                'L': (2, -1, -1), 'M': (2, 0, -1), 'R': (2, 1,  1),
                'U': (1, -1, -1), 'E': (1, 0,  1), 'D': (1, 1,  1),
                'F': (0, -1, -1), 'S': (0, 0, -1), 'B': (0, 1,  1),
                'X': (2,  2,  1), 'Y': (1, 2, -1), 'Z': (0, 2, -1)
                }

        for m in ms:
            axis, slice, dir = mmap[m[0].upper()]

            if "'" in m:
                self.anims.add(Anim(self, axis, slice, -dir, self.speed))

            elif '2' in m:
                self.anims.add(Anim(self, axis, slice, dir, self.speed), Anim(self, axis, slice, dir, self.speed))

            else:
                self.anims.add(Anim(self, axis, slice, dir, self.speed))


    def anim(self): #anim function enables the rotation to be seen in a 3d animated from

        if self.anims.get(0):
            if self.anims.get(0).done:
                self.anims.pop()

            else:
                self.anims.get(0).step()

        elif self.queue.get(0):
            self.move(self.queue.pop())


    def moveX(self, slice, dir=1): #rotate and translates cube pieces parallel to the x-axis

        for p in self.pieces:
            if slice > 1 or p.x == slice:
                t = PMatrix2D()
                t.rotate(dir * HALF_PI)
                t.translate(p.y, p.z)
                p.rX(dir)
                p.pos(round(p.x), round(t.m02), round(t.m12))


    def moveY(self, slice, dir=1): #rotate and translates cube pieces parallel to the y-axis

        for p in self.pieces:
            if slice > 1 or p.y == slice:
                t = PMatrix2D()
                t.rotate(dir * HALF_PI)
                t.translate(p.x, p.z)
                p.rY(dir)
                p.pos(round(t.m02), round(p.y), round(t.m12))


    def moveZ(self, slice, dir=1): #rotate and translates cube pieces parallel to the z-axis

        for p in self.pieces:
            if slice > 1 or p.z == slice:
                t = PMatrix2D()
                t.rotate(dir * HALF_PI)
                t.translate(p.x, p.y)
                p.rZ(dir)
                p.pos(round(t.m02), round(t.m12), round(p.z))
