from sticker import Sticker


class Piece:
    """Handles rendering and updating of a cube piece.

    Args:
        id (int): Unique identifier for the piece assigned by a parent
            cube.
        colors (:obj:`list` of int): Color scheme in `FBUDLR` order.
        x (int): The x-coordinate of the piece.
        y (int): The y-coordinate of the piece.
        z (int): The z-coordinate of the piece.
        sz (int): Size of the piece.

    Attributes:
        id (int): Unique identifier for the piece assigned by a parent
            cube.
        colors (:obj:`list` of int): Color scheme in `FBUDLR` order.
        x (int): The x-coordinate of the piece.
        y (int): The y-coordinate of the piece.
        z (int): The z-coordinate of the piece.
        sz (int): Size of the piece.
        stickers (:obj:`list` of :obj:`Sticker`): Set of stickers on the piece.

    """

    def __init__(self, id, colors, x, y, z, sz):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.sz = sz
        self.stickers = [
                         Sticker(-1,  0,  0, colors[0], self.sz),
                         Sticker( 1,  0,  0, colors[1], self.sz),
                         Sticker( 0, -1,  0, colors[2], self.sz),
                         Sticker( 0,  1,  0, colors[3], self.sz),
                         Sticker( 0,  0, -1, colors[4], self.sz),
                         Sticker( 0,  0,  1, colors[5], self.sz)
                         ]


    def display(self):
        """Displays the piece.

        This method is called inside `Cube.display` during each `draw`
        call (see `pycube.pyde`).
        """

        sz = self.sz

        pushMatrix()

        stroke(0)
        strokeWeight(sz // 10 or 1)
        noFill()
        translate(sz * self.x, sz * self.y, sz * self.z)
        box(sz)

        for s in self.stickers:
            s.display()

        popMatrix()


    def getsticker(self, x, y, z):
        """Finds the sticker with the given (x,y,z) coordinates.

        Used in `Cube.solved` to find centers.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            z (int): The z-coordinate.

        Returns:
            Sticker: The found sticker, or `None` if no sticker matches
                the query.
        """

        for s in self.stickers:
            if (s.x, s.y, s.z) == (x, y, z):
                return s


    def pos(self, x, y, z):
        """Changes the piece position to the given (x,y,z) coordinates.

        Used in `Cube.moveX`, `Cube.moveY`, and `Cube.moveZ` to update
        each piece's position.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            z (int): The z-coordinate.

        """

        self.x = x
        self.y = y
        self.z = z


    def rX(self, dir):
        """Rotates each sticker along the X axis.

        Used in `Cube.moveX` to update each piece's rotation.

        Args:
            dir (int): Direction of rotation (1 for clockwise, -1 for
                counterclockwise).

        """

        for s in self.stickers:
            s.rX(dir * HALF_PI)


    def rY(self, dir):
        """Rotates each sticker along the Y axis.

        Used in `Cube.moveY` to update each piece's rotation.

        Args:
            dir (int): Direction of rotation (1 for clockwise, -1 for
                counterclockwise).

        """

        for s in self.stickers:
            s.rY(dir * HALF_PI)


    def rZ(self, dir):
        """Rotates each sticker along the Y axis.

        Used in `Cube.moveZ` to update each piece's rotation.

        Args:
            dir (int): Direction of rotation (1 for clockwise, -1 for
                counterclockwise).

        """

        for s in self.stickers:
            s.rZ(dir * HALF_PI)
