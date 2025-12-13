import time
from smiley import Smiley

class Angry(Smiley):
    def __init__(self):
        # Initialise with red complexion for Angry
        super().__init__(complexion=self.RED)
        self.draw_angry_face()   # show the angry face immediately

    def draw_mouth(self):
        """
        Draws mouth feature on angry smiley
        """
        mouth = [41, 42, 43, 44, 45, 46]  # straight/downturned mouth pixels
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self):
        """
        Draws red eyes on the angry smiley
        """
        eye_pixels = [10, 13, 18, 21]
        for pixel in eye_pixels:
            self.pixels[pixel] = self.RED

    def draw_angry_face(self):
        """
        Combines mouth and eyes into a full angry face
        """
        # Reset background to complexion colour before drawing
        self.pixels = [self.my_complexion] * 64
        self.draw_mouth()
        self.draw_eyes()
        self.show()
