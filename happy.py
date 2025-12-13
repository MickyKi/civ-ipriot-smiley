import time
from smiley import Smiley
from blinkable import Blinkable

class Happy(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.YELLOW)
        self.draw_happy_face()

    def draw_mouth(self):
        mouth = [41, 46, 50, 51, 52, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        eye_pixels = [10, 13, 18, 21]
        for pixel in eye_pixels:
            colour = self.BLANK if wide_open else self.YELLOW
            self.pixels[pixel] = colour

    def draw_happy_face(self):
        self.pixels = [self.my_complexion] * 64
        self.draw_mouth()
        self.draw_eyes()
        self.show()

    def blink(self, delay=0.25):
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
