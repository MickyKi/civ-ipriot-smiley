import time
from smiley import Smiley

class Happy(Smiley):
    """
    Provides a Smiley with a happy expression
    """
    def __init__(self):
        super().__init__()
        self.draw_happy_face()   # show the happy face immediately

    def draw_mouth(self):
        """
        Renders a smiling mouth by blanking the pixels that form that object.
        """
        mouth = [41, 46, 50, 51, 52, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws the eyes (open or closed) on the happy smiley.
        """
        eye_pixels = [10, 13, 18, 21]
        for pixel in eye_pixels:
            colour = self.BLANK if wide_open else self.YELLOW
            self.pixels[pixel] = colour

    def draw_happy_face(self):
        """
        Combines mouth and eyes into a full happy face
        """
        self.pixels = [self.YELLOW] * 64   # reset background
        self.draw_mouth()
        self.draw_eyes()
        self.show()

    def blink(self, delay=0.25):
        """
        Blinks the happy smiley's eyes once
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
