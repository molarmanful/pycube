from __future__ import division
import time


class Timer:
    """Automatically calculates time elapsed.

    Attributes:
        times (:obj:`list` of float): List of all stored times.
        ing (bool): Whether the timer is running.

    """

    def __init__(self):
        self.times = []
        self.ing = False
        self.__time = 0


    def start(self):
        """Starts the timer."""

        self.ing = True
        self.times.append(0)
        self.__time = time.time()


    def update(self):
        """Updates the timer to reflect current difference in time."""

        if self.ing:
            self.times[-1] = int((time.time() - self.__time) * 1000) / 1000


    def end(self):
        """Stops the timer."""

        self.ing = False
