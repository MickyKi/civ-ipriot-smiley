import time
from smiley import Smiley

class Sad(Smiley):
    def __init__(self):
        super().__init__()
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a sad smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a sad smiley
        :param wide_open: Render eyes wide open or shut
        """
        eye_pixels = [10, 13, 18, 21]
        for pixel in eye_pixels:
            colour = self.BLANK if wide_open else self.YELLOW
            self.pixels[pixel] = colour

    def draw_sad_face(self):
        """
        Combines mouth and eyes into a full sad face
        """
        self.draw_mouth()
        self.draw_eyes()

    def blink(self, delay=0.25):
        """
        Blink by clearing the display, pausing, then redrawing the sad face
        """
        self.sense_hat.clear()   # eyes disappear
        time.sleep(delay)        # short pause
        self.draw_sad_face()     # redraw sad face
        self.show()              # push pixels to display
