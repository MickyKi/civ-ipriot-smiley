from smiley import Smiley

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)
        self.draw_angry_face()

    def draw_mouth(self):
        mouth = [41, 42, 43, 44, 45, 46]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self):
        eye_pixels = [10, 13, 18, 21]
        for pixel in eye_pixels:
            self.pixels[pixel] = self.RED

    def draw_angry_face(self):
        self.pixels = [self.my_complexion] * 64
        self.draw_mouth()
        self.draw_eyes()
        self.show()
