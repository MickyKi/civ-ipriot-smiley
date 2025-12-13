import time
from smiley import Smiley

class Sad(Smiley):
    def __init__(self):
        super().__init__(complexion=self.BLUE)
        self.draw_sad_face()

    def draw_mouth(self):
        """
        Draws a downturned mouth for the sad face.
        """
        mouth = [42, 43, 44, 45]   # neutral line
        corners = [50, 53]         # corners lower for frown
        for pixel in mouth + corners:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        eye_pixels = [10, 13, 18, 21]
        for pixel in eye_pixels:
            colour = self.BLANK if wide_open else self.BLUE
            self.pixels[pixel] = colour

    def draw_sad_face(self):
        self.pixels = [self.my_complexion] * 64
        self.draw_mouth()
        self.draw_eyes()
        self.show()

    def blink(self, delay=1):
        # Close eyes (fill them with blue to match complexion)
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True) # Reopen eyes
        self.show()
