import time
from smiley import Smiley

class Sad(Smiley):
    def __init__(self):
        super().__init__(complexion=self.BLUE)
        self.draw_sad_face()

    def draw_mouth(self):
    # Downturned mouth shape
    mouth = [42, 43, 44, 45]      #i changed these lines to let the sad face have a frown instead of straight line. 
    corners = [41, 46]            #i changed these lines to let the sad face have a frown instead of straight line.
    for pixel in mouth + corners:
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

