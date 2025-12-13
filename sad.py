import time
from smiley import Smiley

class Sad(Smiley):
    def __init__(self):
        super().__init__(complexion=self.BLUE)   # Sad face is blue
        self.draw_sad_face()   # show the sad face immediately

    def draw_mouth(self):
        mouth = [41, 42, 43, 44, 45, 46]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        eye_pixels = [10, 13, 18, 21]
        for pixel in eye_pixels:
            colour = self.BLANK if wide_open else self.YELLOW
            self.pixels[pixel] = colour

    def draw_sad_face(self):
        self.pixels = [self.my_complexion] * 64
        self.draw_mouth()
        self.draw_eyes()
        self.show()

    def blink(self, delay=0.25):
        self.clear()
        time.sleep(delay)
        self.draw_sad_face()
