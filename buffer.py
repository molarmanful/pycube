class Buffer:
    """Creates an offscreen cube for color-based click detection.

    Args:
        colors (:list:`int`): 6 unique colors, 1 for each face.
        sz (int): Size of each piece in the actual cube (default 100).

    Attributes:
        colors (:list:`int`): 6 unique colors, 1 for each face.
        sz (int): Size of each piece in the actual cube (default 100).
        buf (PGraphics): Renderer for the offscreen cube.

    """

    def __init__(self, colors, sz = 100):

        self.colors = colors
        self.sz = 100
        self.buf = createGraphics(width, height, P3D)


    def update(self):
        """Draws the offscreen cube to match the actual cube.

        This method is called alongside `Cube.display` (see `cube.py`)
        during each `draw` call (see `pycube.pyde`).
        """

        colors = self.colors
        sz = self.sz
        buf = self.buf

        buf.beginDraw()

        # Black is the default value to detect if a face is not clicked.
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
            # Render the offscreen cube.
            # Implementation-wise, this is rather similar to how Sticker
            # is rendered, albeit with a 3x size modifier.
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

    def getpixel(self, x, y):
        """Gets the pixel under the given (x,y) coordinates.

        This function is called during each `mousePressed` call (see
        `pycube.pyde`).

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            int: The color of the pixel at (x,y).

        """

        self.buf.loadPixels()
        return self.buf.pixels[y * width + x]
