import random
from piece import Piece
from anim import Anim
from stack import Stack
from timer import Timer


class Cube:
    """Handles rendering and updating of the cube.

    Args:
        colors (:obj:`list` of int): Color scheme in `FBUDLR` order.
        sz (int, optional): Size of each cube piece (default 100).
        speed (int, optional): Animation speed in radians per frame (default .3).

    Attributes:
        colors (:obj:`list` of int): Color scheme in `FBUDLR` order.
        sz (int): Size of each cube piece (default 100).
        speed (int): Animation speed in radians per frame (default .3).
        pieces (:obj:`list` of :obj:`piece.Piece`): Container for all
            cube pieces.
        queue (:py:class:`stack.Stack` of str): Queue for moves that
            need to be executed.
        moved (:py:class:`stack.Stack` of str): Queue for inverses of
            previously executed moves.
        anims (:py:class:`stack.Stack` of :py:class:`anim.Anim`): Queue
            for animations that need to be run.
        timer (:py:class:`timer.Timer`): The timer assigned to the cube.
        timing (bool): Whether a timed attempt is in progress.
        mmode (bool): Whether mouse mode is on.
        moving (bool): Whether the cube is currently animating.
        solving (bool): Whether the cube is currently solving.
        scrambling (bool): Whether the cube is currently scrambling.
        file (open): File to write times to.

    """

    def __init__(self, colors, sz=100, speed=.3):
        self.colors = colors
        self.sz = sz
        self.speed = speed
        self.pieces = []
        self.queue = Stack()
        self.moved = Stack()
        self.anims = Stack()
        self.timer = Timer()
        self.timing = False
        self.mmode = False
        self.moving = False
        self.solving = False
        self.scrambling = False
        self.file = []
        self.disp = False

        open('.timefile.csv', 'a').close() # create file if nonexistent
        self.file = open('.timefile.csv', 'r') # reopen file in read mode
        for l in self.file:
            try:
                self.timer.times.append(float(l))
            except:
                if l == 'DNF':
                    self.timer.times.append('DNF')

        # reopen the file in write mode
        self.file.close()
        self.file = open('.timefile.csv', 'w+')

        id = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if (x, y, z) != (0, 0, 0): # Remove the core piece.
                        # Add pieces to pieces.
                        self.pieces.append(Piece(id, colors, x, y, z, self.sz))
                        id += 1


    def display(self):
        """Displays the cube."""

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


    def anim(self):
        """Prioritizes actions based on the states of the cube's attributes."""

        if self.anims.get(0):
            if self.anims.get(0).done:
                # Remove current animation when done.
                self.anims.pop()
            else:
                # Progress current animation.
                self.anims.get(0).step()

        elif self.solving and self.solved():
            # Reset cube after `Cube.solve()`.
            self.queue.items = []
            self.solving = False

        elif self.queue.get(0):
            if self.timing and not self.scrambling and not self.timer.ing:
                # Start the timer after scrambling.
                self.timer.start()

            # Add queued moves to the animation queues.
            self.move(self.queue.pop())

        elif self.timer.ing and self.solved():
            # Stop the timer.
            self.timer.end()
            self.timing = False

            if self.solved() and self.timer.times[-1] != 'DNF':
                self.disp = True

        self.timer.update()


    def getpiece(self, x, y, z):
        """Finds the piece with the given (x,y,z) coordinates.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            z (int): The z-coordinate.

        Returns:
            The found :py:class:`piece.Piece`, or `None` if no piece
            matches the query.

        """

        for p in self.pieces:
            if (p.x, p.y, p.z) == (x, y, z):
                return p


    def free(self):
        """Checks if the cube is idle and able to be acted upon.

        Returns:
            bool: True if idle, False otherwise.

        """

        return not self.moving and not self.queue.get(0) and not self.anims.get(0)


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


    def best(self):
        """Checks if the last time is a personal best.

        Returns:
            bool: `True` if personal best, `False` otherwise.

        """

        last = self.timer.times[-1]
        return last != 'DNF' and all(last <= t for t in self.timer.times if t != 'DNF')


    def time(self):
        """Sets up a timed solving attempt."""

        self.timing = True
        self.scramble()

        self.disp = False


    def scramble(self, l=25):
        """Scrambles the cube.

        This implementation prevents degenerate cases (i.e. R L R) for
        higher-quality scrambles. Moves are pushed to Cube.queue upon
        generation.

        Args:
            l (int, optional): Length of the scramble (default 25).

        """

        self.scrambling = True

        a = ' '
        b = ' '
        for n in range(l):
            choices = ['RL', 'UD', 'FB']
            for i, m in enumerate(choices):
                if a in m:
                    # Filter out parallel degeneracy (i.e. R L R).
                    choices[i] = m.replace(a, '')
                    if b in m:
                        # Filter out duplicate degeneracy (i.e. R R).
                        choices[i] = ''

            b, a = a, random.choice(''.join(choices))
            self.queue.add(a + random.choice(["'", '2', '']))

        # Add a '#' to the move queue as a special indicator.
        self.queue.add('#')


    def move(self, *ms):
        """Parses cube notation into animations.

        Args:
            *ms: Series of notated moves.

        """

        # Map cube notation to corresponding clockwise movements.
        mmap = {
                'L': (2, -1, -1), 'M': (2, 0, -1), 'R': (2, 1,  1),
                'U': (1, -1, -1), 'E': (1, 0,  1), 'D': (1, 1,  1),
                'F': (0, -1, -1), 'S': (0, 0, -1), 'B': (0, 1,  1),
                'X': (2,  2,  1), 'Y': (1, 2, -1), 'Z': (0, 2, -1)
                }

        for m in ms:
            if m == '#':
                # End the scramble if '#' is found.
                self.scrambling = False
            else:
                axis, slice, dir = mmap[m[0].upper()]
                if "'" in m:
                    # Invert the move.
                    self.anims.add(Anim(self, axis, slice, -dir, self.speed))
                    m = m.replace("'", '')
                elif '2' in m:
                    # Double the move.
                    self.anims.add(Anim(self, axis, slice, dir, self.speed), Anim(self, axis, slice, dir, self.speed))
                else:
                    self.anims.add(Anim(self, axis, slice, dir, self.speed))
                    m = m + "'"

                # Push inverse move to history queue.
                self.moved.push(m)


    def solve(self):
        """Rewinds the cube to a solved state."""

        self.queue.add(*self.moved.items)
        self.solving = True
        self.moved.items = []


    def moveX(self, slice, dir=1):
        """Alters cube state via unanimated X rotation.

        This method is called after an animation finishes. It affects
        piece positions, translations, and rotations.

        Args:
            slice (int): The slice to rotate. If slice is 2, then all
                slices will rotate simultaneously.
            dir (int, optional): Direction of rotation (1 for clockwise,
                -1 for counterclockwise).

        """

        for p in self.pieces:
            if slice > 1 or p.x == slice: # Filter pieces not in slice.
                # Use PMatrix2D() to calculate position from rotation.
                t = PMatrix2D()
                t.rotate(dir * HALF_PI)
                t.translate(p.y, p.z)
                p.rX(dir)
                p.pos(round(p.x), round(t.m02), round(t.m12))


    def moveY(self, slice, dir=1):
        """Alters cube state via unanimated Y rotation.

        This method is called after an animation finishes. It affects
        piece positions, translations, and rotations.

        Args:
            slice (int): The slice to rotate. If slice is 2, then all
                slices will rotate simultaneously.
            dir (int, optional): Direction of rotation (1 for clockwise,
                -1 for counterclockwise).

        """

        for p in self.pieces: # Filter pieces not in slice.
            if slice > 1 or p.y == slice:
                # Use PMatrix2D() to calculate position from rotation.
                t = PMatrix2D()
                t.rotate(dir * HALF_PI)
                t.translate(p.x, p.z)
                p.rY(dir)
                p.pos(round(t.m02), round(p.y), round(t.m12))


    def moveZ(self, slice, dir=1):
        """Alters cube state via unanimated Z rotation.

        This method is called after an animation finishes. It affects
        piece positions, translations, and rotations.

        Args:
            slice (int): The slice to rotate. If slice is 2, then all
                slices will rotate simultaneously.
            dir (int, optional): Direction of rotation (1 for clockwise,
                -1 for counterclockwise).

        """

        for p in self.pieces: # Filter pieces not in slice.
            if slice > 1 or p.z == slice:
                # Use PMatrix2D() to calculate position from rotation.
                t = PMatrix2D()
                t.rotate(dir * HALF_PI)
                t.translate(p.x, p.y)
                p.rZ(dir)
                p.pos(round(t.m02), round(t.m12), round(p.z))
