class Anim:
    """Handles animation stepping for each 90-degree turn of the cube.

    Args:
        cube (Cube): Parent cube.
        axis (int): Axis of rotation (0 for X, 1 for Y, and 2 for Z).
        slice (int): Slice to be rotated (-1 <= n <= 1).
        dir (int): Direction of rotation (1 for clockwise, -1 for
            counterclockwise).
        speed (float, optional): Speed of rotation in radians per frame (default
            .3).

    Attributes:
        cube (Cube): Parent cube.
        axis (int): Axis of rotation (0 for X, 1 for Y, and 2 for Z).
        slice (int): Slice to be rotated (-1 <= n <= 1).
        dir (int): Direction of rotation (1 for clockwise, -1 for
            counterclockwise).
        speed (float): Speed of rotation in radians per frame (default
            .3).
        rot (float): Current angle of rotation in radians.
        ing (bool): Whether the animation is in progress.
        done (bool): Whether the animation has finished.

    """

    def __init__(self, cube, axis, slice, dir, speed=.3):
        self.cube = cube
        self.axis = axis
        self.slice = slice
        self.dir = dir
        self.speed = speed
        self.rot = 0
        self.ing = True
        self.done = False


    def step(self):
        """Progresses the animation by `speed` radians.

        This method is called from the animation stack
        (:py:attr:`cube.Cube.anims`) during each `draw` call (see
        `pycube.pyde`). After `PI / 2` radians (90deg), the animation
        stops and the cube is updated to match the rotation.
        """

        if self.ing:
            # Progress the animation.
            self.rot += self.dir * self.speed
            self.cube.moving = True

            if abs(self.rot) > HALF_PI:
                # Stop the rotation animation.
                self.rot = 0
                self.ing = False
                self.done = True
                self.cube.moving = False

                # Update the cube to match the rotation.
                # This is because the pieces don't actually stay after
                # the animation is finished, thus requiring an unseen
                # adjustment to the cube post-animation.
                if self.axis == 2:
                    self.cube.moveZ(self.slice, self.dir)
                elif self.axis == 1:
                    self.cube.moveY(self.slice, -self.dir)
                else:
                    self.cube.moveX(self.slice, self.dir)
