import time
from smiley import Smiley
from blinkable import Blinkable

class Happy(Smiley, Blinkable):
    def __init__(self):
        # Initialise with complexion
        super().__init__(complexion=self.YELLOW)
        self.draw_happy_face()   # show the happy face immediately

    def draw_mouth(self):
        """
        Renders a smiling mouth by blanking the pixels that form that object.
        """
        mouth = [41, 46, 50, 51, 52, 53]  # upturned mouth pixels
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws the eyes (open or closed) on the happy smiley.
        :param wide_open: Render eyes wide open or shut
        """
        eye_pixels = [10, 13, 18, 21]
        for pixel in eye_pixels:
            colour = self.BLANK if wide_open else self.YELLOW
            self.pixels[pixel] = colour

    def draw_happy_face(self):
        """
        Combines mouth and eyes into a full happy face
        """
        # Reset background to complexion before drawing
        self.pixels = [self.my_complexion] * 64
        self.draw_mouth()
        self.draw_eyes()
        self.show()

    def blink(self, delay=0.25):
        """
        Blinks the happy smiley's eyes once.
        Uses Blinkable dimming behaviour for consistency.
        """
        super().blink(delay)
